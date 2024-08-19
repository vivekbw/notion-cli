from datetime import datetime
from click.testing import CliRunner
from notion_cli.cli import send, read, format_timestamp, search


def test_send_message(mock_request=None):
    """Test Case 1: Sending a normal message"""
    runner = CliRunner()

    if mock_request:
        result = runner.invoke(send, mock_request)
        assert result.exit_code == 0
        return

    sender = 'Vivek'
    recipient = 'Christopher'
    message = 'Hello, World!'
    timestamp = datetime.now().isoformat()

    result = runner.invoke(send, [sender, recipient, message, timestamp])

    assert result.exit_code == 0
    assert f"\nMessage sent from {sender} to {recipient} at {format_timestamp(timestamp)}\n" == result.output


def test_send_message_missing_args():
    """Test Case 2: Sending a message without contents and timestamp"""
    runner = CliRunner()

    result = runner.invoke(send, ['Vivek', 'Christopher'])

    assert result.exit_code != 0
    assert "Error: Missing argument" in result.output


def test_read_message():
    """Test Case 3: Reading a message"""
    runner = CliRunner()

    sender = 'Tom'
    recipient = 'Jerry'
    message = 'Run!'
    timestamp = datetime.now().isoformat()

    test_send_message([sender, recipient, message, timestamp])

    read_result = runner.invoke(read, [recipient])

    assert read_result.exit_code == 0
    assert message in read_result.output
    assert sender in read_result.output
    assert format_timestamp(timestamp) in read_result.output


def test_search_no_results():
    """Test Case 4: Making a search requrest with no results"""
    runner = CliRunner()

    result = runner.invoke(search, ['NO_RESULTS_FOR_THIS_SEARCH'])

    assert result.exit_code == 0
    assert "No messages containing 'NO_RESULTS_FOR_THIS_SEARCH' found!" in result.output


def test_search_case_insensitivity():
    """Test Case 5: Search for messages with case insensitivity"""
    runner = CliRunner()

    sender = 'Vivek'
    recipient = 'Gavin'
    message = 'cAsE sEnsItIviTy Test'
    timestamp = datetime.now().isoformat()

    test_send_message([sender, recipient, message, timestamp])

    search_result = runner.invoke(search, ['case sensitivity'])

    assert search_result.exit_code == 0
    assert message in search_result.output
    assert sender in search_result.output
    assert recipient in search_result.output
    assert format_timestamp(timestamp) in search_result.output
