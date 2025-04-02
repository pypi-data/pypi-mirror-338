import asyncio
from unittest.mock import AsyncMock, patch

import pytest

from lw2.lightware import (
    InvalidInputNumber,
    InvalidOutputNumber,
    InvalidPresetNumber,
    InvalidResponse,
    InvalidValue,
    LightwareLW2,
)


@pytest.fixture()
def lw() -> LightwareLW2:
    return LightwareLW2("localhost")


@pytest.mark.asyncio
async def test_connect(lw):
    """Test the connect method with mocked asyncio.open_connection."""

    with patch(
        "asyncio.open_connection", new_callable=AsyncMock
    ) as mock_open_connection:
        # Mock reader and writer
        mock_reader = AsyncMock()
        mock_writer = AsyncMock()
        mock_open_connection.return_value = (mock_reader, mock_writer)

        mock_writer.wait_closed = AsyncMock()

        await lw.connect()

        # Ensure the connection was established
        mock_open_connection.assert_called_once_with("localhost", 10001)

        # Check if reader and writer were set
        assert lw.reader == mock_reader
        assert lw.writer == mock_writer

        await lw.close()

        mock_writer.wait_closed.assert_awaited_once()


@pytest.mark.asyncio
async def test_read_responses(lw):
    """Test the _get_response method by mocking the reader."""
    #
    # Mocking reader and writer
    lw.reader = AsyncMock()
    lw.writer = AsyncMock()

    lw.reader.readline.side_effect = [
        b"foo\r\n",
        b"bar\r\n",
        b"",
    ]

    responses = await lw.read_responses()
    assert responses == ["foo", "bar"]


@pytest.mark.asyncio
async def test_read_responses_timeout(lw):
    """Test that _get_response raises a timeout error."""

    lw.reader = AsyncMock()
    lw.writer = AsyncMock()

    lw.reader.readline = AsyncMock(side_effect=asyncio.TimeoutError)
    lw.timeout = 1  # Set a low timeout to trigger the exception

    responses = await lw.read_responses()
    assert responses is None


def test_extract_response_success(lw):
    response = lw.extract_response("(foo)")
    assert response == "foo"


def test_extract_response_invalid(lw):
    with pytest.raises(InvalidResponse, match=r"unknown response: 'foobar'"):
        lw.extract_response("foobar")


def test_extract_response_invalid_input_number(lw):
    with pytest.raises(InvalidInputNumber):
        lw.extract_response("(ERR01)")


def test_extract_response_invalid_output_number(lw):
    with pytest.raises(InvalidOutputNumber):
        lw.extract_response("(ERR02)")


def test_extract_response_invalid_value(lw):
    with pytest.raises(InvalidValue):
        lw.extract_response("(ERR03)")


def test_extract_response_invalid_preset_number(lw):
    with pytest.raises(InvalidPresetNumber):
        lw.extract_response("(ERR04)")


def test_extract_response_invalid_error(lw):
    with pytest.raises(InvalidResponse, match=r"unknown error: 08"):
        lw.extract_response("(ERR08)")


def test_input_output(lw: LightwareLW2):
    lw.dispatch_handler("O05 I01")
    output = lw.outputs[4]
    assert output.idx == 5
    assert lw.mapping[output].idx == 1

    lw.dispatch_handler("O08 I05")
    output = lw.outputs[7]
    assert output.idx == 8
    assert lw.mapping[output].idx == 5


def test_input_all(lw: LightwareLW2):
    lw.dispatch_handler("I02 ALL")
    for input in lw.mapping.values():
        assert input.idx == 2


def test_query_connection(lw: LightwareLW2):
    lw.dispatch_handler("ALL M02 L02 U02 05 05 05 08 08 08 08 08 08 08 08 08 08")

    output_states = [
        {"muted": True, "locked": False},  # M02
        {"muted": False, "locked": True},  # L02
        {"muted": True, "locked": True},  # U02
    ] + [{"muted": False, "locked": False}] * 13

    expected_inputs = [2, 2, 2, 5, 5, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

    # Test output states
    for output, expected_state in zip(lw.outputs, output_states):
        assert output.muted == expected_state["muted"]
        assert output.locked == expected_state["locked"]

    # Test input mappings
    for output, expected_input in zip(lw.outputs, expected_inputs):
        mapped_input = lw.mapping[output]
        assert mapped_input.idx == expected_input


def test_input_status(lw):
    lw.dispatch_handler("ISD 10000000100100010000000000000000")

    expected_connections = (
        [True] + 7 * [False] + [True, False, False, True, False, False, False, True]
    )

    for input, expected_status in zip(lw.inputs, expected_connections):
        assert input.connected == expected_status


def test_output_status(lw):
    lw.dispatch_handler("OSD 010000001011000000000000000000000")

    expected_connections = (
        [False, True]
        + 6 * [False]
        + [True, False, True, True, False, False, False, False]
    )

    for output, expected_status in zip(lw.outputs, expected_connections):
        assert output.connected == expected_status


def test_mac_handler(lw: LightwareLW2):
    lw.dispatch_handler("MAC_ADDR=00-20-4A-E3-1D-E4")
    assert lw.mac == "00:20:4A:E3:1D:E4"


def test_serial_handler(lw: LightwareLW2):
    lw.dispatch_handler("SN:3C019935")
    assert lw.serial == "3C019935"


def test_firmware_handler(lw: LightwareLW2):
    lw.dispatch_handler("FW:2.5.0")
    assert lw.firmware == "2.5.0"


def test_web_version_handler(lw: LightwareLW2):
    lw.dispatch_handler("WEB_VER=1.4.1")
    assert lw.web_version == "1.4.1"


def test_server_version_handler(lw: LightwareLW2):
    lw.dispatch_handler("SERVER_VER=1.1.5")
    assert lw.server_version == "1.1.5"


def test_product_type_handler(lw: LightwareLW2):
    lw.dispatch_handler("MX16x16DVI-Plus")
    assert lw.product_type == "MX16x16DVI-Plus"


def test_unknown_input(lw):
    lw.dispatch_handler("foobar")
