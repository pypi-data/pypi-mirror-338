from lw2.commands import (
    QueryLAN,
    QueryFirmwareVersion,
    QuerySerialNumber,
    QueryOutputPortStatus,
    QueryInputPortStatus,
    QueryConnections,
    InputToAll,
    InputToOutput,
)


def test_switch_input_to_output():
    command = InputToOutput(in_num=5, out_num=3)
    assert str(command) == "05@03"


def test_switch_input_to_all():
    command = InputToAll(in_num=8)
    assert str(command) == "08@O"


def test_query_connection():
    command = QueryConnections()
    assert str(command) == "VC"


def test_input_port_status():
    command = QueryInputPortStatus()
    assert str(command) == ":ISD"


def test_output_port_status():
    command = QueryOutputPortStatus()
    assert str(command) == ":OSD"


def test_serial():
    command = QuerySerialNumber()
    assert str(command) == "S"


def test_lan_ver():
    command = QueryLAN()
    assert str(command) == "LAN_VER=?"


def test_firmware():
    command = QueryFirmwareVersion()
    assert str(command) == "F"
