from dataclasses import dataclass
from enum import Enum


@dataclass
class Command:
    """
    Command interface for Lightware LW2.
    Each command must implement __str__(), returning the exact
    string to be sent over TCP, without curly braces, e.g. '1@5'.
    """


class Query(Enum):
    CONNECTIONS = "VC"
    INPUTPORTSTATUS = ":ISD"
    OUTPUTPORTSTATUS = ":OSD"
    PRODUCTTYPE = "I"
    SERIAL = "S"
    FIRMWARE = "F"
    LAN = "LAN_VER=?"


@dataclass
class InputToOutput(Command):
    """
    Switch input <in_num> to output <out_num>.
    This corresponds to the LW2 command {<in>@<out>}.
    """

    in_num: int
    out_num: int

    def __str__(self) -> str:
        return f"{self.in_num:02d}@{self.out_num:02d}"


@dataclass
class InputToAll(Command):
    """
    Switch input <in_num> to all outputs.
    This corresponds to the LW2 command {<in>@O}.
    """

    in_num: int

    def __str__(self) -> str:
        return f"{self.in_num:02d}@O"


@dataclass
class QueryConnections(Command):
    """
    Query all outputs' connections.
    LW2 command: {VC}
    """

    def __str__(self) -> str:
        return Query.CONNECTIONS.value


@dataclass
class QueryInputPortStatus(Command):
    """
    Query the status of the input ports
    LW2 command: {:ISD}
    """

    def __str__(self) -> str:
        return Query.INPUTPORTSTATUS.value


@dataclass
class QueryOutputPortStatus(Command):
    """
    Query the status of the input ports
    LW2 command: {:OSD}
    """

    def __str__(self) -> str:
        return Query.OUTPUTPORTSTATUS.value


@dataclass
class QueryProductType(Command):
    """
    Query the type of the device
    LW2 command: {I}
    """

    def __str__(self) -> str:
        return Query.PRODUCTTYPE.value


@dataclass
class QuerySerialNumber(Command):
    """
    Query the serial number of the device
    LW2 command: {S}
    """

    def __str__(self) -> str:
        return Query.SERIAL.value


@dataclass
class QueryFirmwareVersion(Command):
    """
    Query the CPU firmware version of the device
    LW2 command: {F}
    """

    def __str__(self) -> str:
        return Query.FIRMWARE.value


@dataclass
class QueryLAN(Command):
    """
    Query the network controller of the device
    LW2 command: {LAN_VER=?}
    """

    def __str__(self) -> str:
        return Query.LAN.value
