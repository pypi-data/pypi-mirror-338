import asyncio
import logging
import re
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional

from lw2.commands import (
    Command,
    InputToAll,
    InputToOutput,
    QueryConnections,
    QueryInputPortStatus,
    QueryLAN,
    QueryOutputPortStatus,
    QueryProductType,
    QuerySerialNumber,
    QueryFirmwareVersion,
)
from lw2.handler import (
    FirmwareResponse,
    InputStatusResponse,
    InputToAllResponse,
    InputToOutputResponse,
    MacAddressResponse,
    OutputStatusResponse,
    ProductTypeResponse,
    QueryConnectionResponse,
    SerialNumberResponse,
    ServerVersionResponse,
    WebVersionResponse,
)

_LOGGER = logging.getLogger(__name__)


class LightwareLW2Error(Exception):
    """Generic Lightware LW2 error"""


class ConnectionError(LightwareLW2Error):
    """An error in the underlying socket connection"""


class InvalidInputNumber(LightwareLW2Error):
    """Given input number exceeds the maximum number of inputs or equals zero."""


class InvalidOutputNumber(LightwareLW2Error):
    """Given output number exceeds the installed number of outputs or equals zero."""


class InvalidValue(LightwareLW2Error):
    """Given value exceeds the maximum allowed value can be sent."""


class InvalidPresetNumber(LightwareLW2Error):
    """Given preset number exceeds the maximum allowed preset number."""


class InvalidResponse(Exception):
    """Error while parsing the LW2 response"""


class Type(Enum):
    INPUT = 1
    OUTPUT = 2


@dataclass
class Port:
    idx: int
    type: Type
    connected: bool | None = None

    def __init__(self, idx):
        self.idx = idx

    def __hash__(self):
        return hash(self.idx)

    def __eq__(self, other):
        if not isinstance(other, Port):
            return False
        return self.idx == other.idx and self.type == other.type

    def __str__(self):
        status = "❎" if self.connected else "❌"

        return f"{self.type.name[0]}{self.idx}{status}"

    def __repr__(self):
        return self.__str__()


class Input(Port):
    type = Type.INPUT


class Output(Port):
    type = Type.OUTPUT
    muted: bool = False
    locked: bool = False


@dataclass
class LightwareLW2:
    """
    Lightware LW2 Protocol handler over TCP, using the LW2Command interface.
    """

    RE_RESPONSE = re.compile(r"\((.*)\)")  # e.g. (`(ALL 01010101)`)
    RE_ERROR = re.compile(r"ERR(\d{2})")  # e.g. (`ERR02`)

    def __init__(
        self,
        host: str,
        port: int = 10001,
        num_inputs: int = 16,
        num_outputs: int = 16,
        timeout: int = 1,
    ):
        self.host: str = host
        self.port: int = port
        self.serial: str | None = None
        self.mac: str | None = None
        self.web_version: str | None = None
        self.server_version: str | None = None
        self.product_type: str | None = None
        self.firmware: str | None = None
        self.timeout: int = timeout
        self.num_inputs: int = num_inputs
        self.num_outputs: int = num_outputs
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None

        self.inputs: list[Input] = [Input(i + 1) for i in range(num_inputs)]
        self.outputs: list[Output] = [Output(i + 1) for i in range(num_outputs)]
        self.mapping: Dict[Output, Optional[Input]] = {o: None for o in self.outputs}

        self.response_handlers = [
            InputToOutputResponse,
            InputToAllResponse,
            QueryConnectionResponse,
            InputStatusResponse,
            OutputStatusResponse,
            MacAddressResponse,
            FirmwareResponse,
            WebVersionResponse,
            ServerVersionResponse,
            SerialNumberResponse,
            ProductTypeResponse,
        ]

    async def connect(self) -> None:
        """Establish an async connection to the Lightware device."""
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        _LOGGER.debug(f"Connected to {self.host}:{self.port}")

    @property
    def connected(self) -> bool:
        return all((self.reader, self.writer))

    @property
    def device_data_available(self) -> bool:
        """boolean status if basic device information have been fetched"""
        return all(
            (
                self.serial,
                self.mac,
                self.firmware,
                self.server_version,
                self.product_type,
            )
        )

    async def close(self) -> None:
        """Close the async connection."""
        try:
            if self.writer:
                self.writer.close()
                await asyncio.wait_for(self.writer.wait_closed(), timeout=self.timeout)
                _LOGGER.debug(f"Disconnected from {self.host}:{self.port}")
        except asyncio.TimeoutError:
            _LOGGER.warning("Timed out waiting for writer to close.")
        finally:
            self.reader, self.writer = None, None

    async def send_request(self, payload: str):
        if not self.connected:
            await self.connect()
        _LOGGER.debug(f"Sending: {payload!r}")
        self.writer.write(payload.encode("ascii"))
        await self.writer.drain()

    async def update(self) -> None:
        cmds = [
            QueryConnections(),
            QueryInputPortStatus(),
            QueryOutputPortStatus(),
            QueryProductType(),
            QuerySerialNumber(),
            QueryFirmwareVersion(),
            QueryLAN(),
        ]
        await self.send_batch_commands(cmds)

    async def switch(self, input_index: int, output_index: int):
        cmd = InputToOutput(input_index, output_index)
        await self.send_command(cmd)

    async def switch_all(self, input_index: int):
        cmd = InputToAll(input_index)
        await self.send_command(cmd)

    async def send_command(self, command: Command) -> None:
        """
        Send a command and update internal state
        """
        raw_cmd = str(command)

        cmd_str = f"{{{raw_cmd}}}\r\n"
        await self.send_request(cmd_str)
        await self.handle_response()

    async def send_batch_commands(self, commands: list[Command]) -> None:
        """
        Sends all commands in batched mode and update internal state
        """
        cmd_str = "".join([f"{{{str(command)}}}" for command in commands])
        cmd_str = f"{cmd_str}\r\n"
        await self.send_request(cmd_str)
        await self.handle_response()

    async def handle_response(self) -> None:
        responses = await self.read_responses()
        if responses:
            for response in responses:
                content = self.extract_response(response)
                self.dispatch_handler(content)

    async def read_responses(self) -> Optional[list[str]]:
        if not self.connected:
            raise ConnectionError("Not connected")

        responses = []
        try:
            while self.connected:
                line = await asyncio.wait_for(
                    self.reader.readline(), timeout=self.timeout
                )
                _LOGGER.debug(f"Received {line!r}")
                if not line:
                    break

                responses.append(line.decode("ascii").rstrip("\r\n"))
        except asyncio.TimeoutError:
            pass
        finally:
            await self.close()

            if not responses:
                return None

            return responses

    def extract_response(self, response: str) -> str:
        """
        Extracts the content of the response.
        Inspect the response for LW2 error codes like (ERR01).
        """
        response_match = self.RE_RESPONSE.match(response)
        if not response_match:
            raise InvalidResponse(f"unknown response: {response!r}")

        content: str = response_match.group(1)
        self._check_for_error(content)

        return content

    def _check_for_error(self, content: str):
        err_match = self.RE_ERROR.match(content)

        if err_match:
            err_code = err_match.group(1)
            match err_code:
                case "01":
                    raise InvalidInputNumber()
                case "02":
                    raise InvalidOutputNumber()
                case "03":
                    raise InvalidValue()
                case "04":
                    raise InvalidPresetNumber()
                case _:
                    raise InvalidResponse(f"unknown error: {err_code}")

    def dispatch_handler(self, response: str) -> None:
        """
        Dispatches the response based on the pattern to the matched handler
        """
        _LOGGER.debug(f"Handling response: {response!r}")

        for handler in self.response_handlers:
            if match := re.match(handler.pattern(), response):
                return handler.handle_match(self, match)

        _LOGGER.warning(f"Invalid message format: {response}")
