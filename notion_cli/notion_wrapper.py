import os
from notion_client import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.environ["NOTION_TOKEN"])

"""
------------------------------------------------------------------------------------
                                Helper Methods
------------------------------------------------------------------------------------
"""


def get_database_id():
    """
    If the CLI is being run in a test environment (pytest), this method
    returns the test database ID. Otherwise, it returns the production
    database ID
    """
    if os.getenv("PYTEST_ENVIRONMENT"):
        return os.getenv("TEST_DATABASE_ID")
    return os.getenv("PROD_DATABASE_ID")


def format_timestamp(timestamp):
    """
    Formats a ISO 8601 timestamp into a more readable format

    Args:
        timestamp:
            A string of timestamp in ISO 8601 format
            ex: '2024-08-18T09:00:00'

    Returns:
        A string of the formatted timestamp, e.g: 'August 18th, 9:00am'
    """
    timestamp_obj = datetime.fromisoformat(timestamp)
    day = timestamp_obj.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    return timestamp_obj.strftime(f"%B {day}{suffix}, %I:%M%p").replace(" 0", " ").replace("AM", "am").replace("PM", "pm")


"""
------------------------------------------------------------------------------------
                                    CLI Methods
------------------------------------------------------------------------------------
"""


def send_message(sender, recipient, message, timestamp):
    """Sends a message from [sender] to [recipient]"""
    DATABASE_ID = get_database_id()
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Sender": {"rich_text": [{"text": {"content": sender}}]},
            "Recipient": {"rich_text": [{"text": {"content": recipient}}]},
            "Timestamp": {"date": {"start": timestamp}},
            "Message": {"title": [{"text": {"content": message}}]},
        }
    )


def read_messages(recipient):
    """Reads all messages sent to [recipient]"""
    DATABASE_ID = get_database_id()
    results = notion.databases.query(
        **{
            "database_id": DATABASE_ID,
            "filter": {
                "property": "Recipient",
                "rich_text": {"equals": recipient},
            },
        }
    )

    formatted_messages = []

    for r in results["results"]:
        sender = r["properties"]["Sender"]["rich_text"][0]["text"]["content"]
        message = r["properties"]["Message"]["title"][0]["text"]["content"]
        timestamp = r["properties"]["Timestamp"]["date"]["start"]

        formatted_timestamp = format_timestamp(timestamp)

        formatted_messages.append({
            "sender": sender,
            "message": message,
            "timestamp": formatted_timestamp
        })

    return formatted_messages


def search_messages(phrase):
    """Searches for messages containing [phrase]"""
    DATABASE_ID = get_database_id()
    results = notion.databases.query(
        **{
            "database_id": DATABASE_ID,
            "filter": {
                "property": "Message",
                "text": {"contains": phrase},
            },
        }
    )

    formatted_messages = []

    for r in results["results"]:
        sender = r["properties"]["Sender"]["rich_text"][0]["text"]["content"]
        recipient = r["properties"]["Recipient"]["rich_text"][0]["text"]["content"]
        message = r["properties"]["Message"]["title"][0]["text"]["content"]
        timestamp = r["properties"]["Timestamp"]["date"]["start"]

        formatted_timestamp = format_timestamp(timestamp)

        formatted_messages.append({
            "sender": sender,
            "recipient": recipient,
            "message": message,
            "timestamp": formatted_timestamp
        })

    return formatted_messages


def clear_database():
    """Clears all entries in the Notion database"""
    DATABASE_ID = get_database_id()
    results = notion.databases.query(database_id=DATABASE_ID)

    for page in results["results"]:
        notion.pages.update(page_id=page["id"], archived=True)
