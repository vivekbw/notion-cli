import click
from notion_cli.notion_wrapper import send_message, read_messages, search_messages, format_timestamp, clear_database, delete_message


@click.group()
def cli():
    """This method groups all commands within a single CLI"""
    pass


@cli.command()
@click.argument('sender')
@click.argument('recipient')
@click.argument('message')
@click.argument('timestamp')
def send(sender, recipient, message, timestamp):
    """Sends [message] from [sender] to [recipient] at [timestamp]"""
    send_message(sender, recipient, message, timestamp)
    click.echo(
        f"\nMessage sent from {sender} to {recipient} at {format_timestamp(timestamp)}")


@cli.command()
@click.argument('recipient')
def read(recipient):
    """Reads all messages sent to [recipient]"""
    messages = read_messages(recipient)
    if not messages:
        click.echo(f"\nNo messages for {recipient}!\n")
    else:
        click.echo(f"\nMessages for {recipient}: \n")
        for i, msg in enumerate(messages):
            click.echo(f"|Message {i+1}: {msg['message']}")
            click.echo(f"|From: {msg['sender']}")
            click.echo(f"|Sent at: {msg['timestamp']}\n")


@cli.command()
@click.argument('phrase')
def search(phrase):
    """Search for messages containing a specific [phrase]"""
    messages = search_messages(phrase)

    if not messages:
        click.echo(f"\nNo messages containing '{phrase}' found!\n")
    else:
        click.echo(f"\nMessages containing '{phrase}': \n")
        for i, msg in enumerate(messages):
            click.echo(f"|Message {i+1}: {msg['message']}")
            click.echo(f"|From: {msg['sender']}")
            click.echo(f"|To: {msg['recipient']}")
            click.echo(f"|Sent at: {msg['timestamp']}\n")


@cli.command()
@click.argument('message_id')
def delete(message_id):
    """Deletes a message with the specified ID"""
    if delete_message(message_id):
        click.echo(f"\nMessage with ID {message_id} has been deleted.")
    else:
        click.echo(f"\nNo message found with ID {message_id}.")


@cli.command()
def clear():
    """Clears all messages in the database"""
    clear_database()


if __name__ == '__main__':
    cli()
