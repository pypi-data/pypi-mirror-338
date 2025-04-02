import abc
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lw2.lightware import LightwareLW2


class Handler(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def pattern() -> re.Pattern[str]:
        """The pattern to match on the response"""
        pass

    @staticmethod
    @abc.abstractmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        """Handle the response and update Lightware object"""
        pass


class InputToOutputResponse(Handler):
    RE = re.compile(r"O(\d{2}) I(\d{2})")

    @staticmethod
    def pattern():
        return InputToOutputResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        input_str, output_str = match.groups()

        output_idx = int(input_str)
        input_idx = int(output_str)

        if 1 <= output_idx <= lw.num_outputs and 1 <= input_idx <= lw.num_inputs:
            output = lw.outputs[output_idx - 1]
            input = lw.inputs[input_idx - 1]
            lw.mapping[output] = input
        else:
            raise ValueError(
                f"Output index {output_idx} out of range (1-{lw.num_outputs})"
            )


class InputToAllResponse(Handler):
    RE = re.compile(r"I(\d{2}) ALL")

    @staticmethod
    def pattern():
        return InputToAllResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        input_str = match.groups()[0]
        input_idx = int(input_str)

        if 1 <= input_idx <= lw.num_inputs:
            input = lw.inputs[input_idx - 1]

            for o in lw.mapping:
                lw.mapping[o] = input
        else:
            raise ValueError(
                f"Input index {input_idx} out of range (1-{lw.num_inputs})"
            )


class QueryConnectionResponse(Handler):
    RE = re.compile(r"ALL\s*((?:[MLU]?\d{2}\s*)+)")

    @staticmethod
    def pattern():
        return QueryConnectionResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        query_response = match.groups()[0]
        inputs = query_response.split()

        if len(inputs) != lw.num_outputs:
            raise ValueError(
                f"Wrong number of outputs. Got {len(inputs)}, Expected: {lw.num_outputs}"
            )

        prefix_states = {
            "M": {"muted": True, "locked": False},
            "L": {"muted": False, "locked": True},
            "U": {"muted": True, "locked": True},
        }

        for output, input_str in zip(lw.outputs, inputs):
            prefix = input_str[0] if input_str[0] in "MLU" else ""
            idx = input_str[1:] if prefix else input_str
            idx = int(idx)

            input = lw.inputs[idx - 1]
            lw.mapping[output] = input

            if prefix:
                states = prefix_states[prefix]
                output.muted = states["muted"]
                output.locked = states["locked"]
            else:
                output.muted = False
                output.locked = False


class InputStatusResponse(Handler):
    RE = re.compile(r"ISD (\d{16}|\d{12}|\d{9})\d{16,23}")

    @staticmethod
    def pattern():
        return InputStatusResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        input_status = match.groups()[0]
        inputs = list(input_status[0 : lw.num_inputs])
        for idx, i in enumerate(inputs):
            connected = i == "1"
            lw.inputs[idx].connected = connected


class OutputStatusResponse(Handler):
    RE = re.compile(r"OSD (\d{16}|\d{12}|\d{9})\d{16,23}")

    @staticmethod
    def pattern():
        return OutputStatusResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        output_status = match.groups()[0]
        outputs = list(output_status[0 : lw.num_outputs])

        for idx, i in enumerate(outputs):
            connected = i == "1"
            lw.outputs[idx].connected = connected


class ProductTypeResponse(Handler):
    RE = re.compile(r"(MX[A-Za-z0-9\-]*)")

    @staticmethod
    def pattern():
        return ProductTypeResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        lw.product_type = match.groups()[0]


class SerialNumberResponse(Handler):
    RE = re.compile(r"SN:([A-Za-z0-9]*)")

    @staticmethod
    def pattern():
        return SerialNumberResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        lw.serial = match.groups()[0]


class FirmwareResponse(Handler):
    RE = re.compile(r"FW:([0-9\.]*)")

    @staticmethod
    def pattern():
        return FirmwareResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        lw.firmware = match.groups()[0]


class MacAddressResponse(Handler):
    RE = re.compile(r"MAC_ADDR=(([0-9A-Fa-f]{2}\-){5}([0-9A-Fa-f]){2})")

    @staticmethod
    def pattern():
        return MacAddressResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        lw.mac = match.groups()[0].replace("-", ":")


class WebVersionResponse(Handler):
    RE = re.compile(r"WEB_VER=([0-9\.]*)")

    @staticmethod
    def pattern():
        return WebVersionResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        lw.web_version = match.groups()[0]


class ServerVersionResponse(Handler):
    RE = re.compile(r"SERVER_VER=([0-9\.]*)")

    @staticmethod
    def pattern():
        return ServerVersionResponse.RE

    @staticmethod
    def handle_match(lw: "LightwareLW2", match: re.Match[str]) -> None:
        lw.server_version = match.groups()[0]
