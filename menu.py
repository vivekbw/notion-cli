"""
Menu for the NotionMail CLI
"""
import subprocess
import sys
from datetime import datetime
from notion_cli.notion_wrapper import get_all_messages, delete_message
import notion_cli


def print_menu():
    print("----------------------------")
    print("\nMenu:")
    print("Type 'send' to send a message")
    print("Type 'read' to read messages")
    print("Type 'search' to search for a message")
    print("Type 'delete' to delete a message")
    print("Type 'clear' to clear all messages")
    print("Type 'exit' to close the menu\n")

    choice = input("Choose an option: ").strip().lower()
    return choice


def send_message():
    sender = input("Enter the sender's name: ")
    recipient = input("Enter the recipient's name: ")
    message = input("Enter the message: ")
    timestamp = datetime.now().isoformat()

    try:
        subprocess.run([sys.executable, "-m", "notion_cli.cli",
                       "send", sender, recipient, message, timestamp], check=True)
        print("Message sent successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Failed to send message: {e}")


def read_messages():
    user = input("Enter the user's name: ")

    try:
        subprocess.run([sys.executable, "-m", "notion_cli.cli",
                       "read", user], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to read messages: {e}")


def search_messages():
    phrase = input("Enter the phrase to search for: ")

    try:
        subprocess.run([sys.executable, "-m", "notion_cli.cli",
                       "search", phrase], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to search messages: {e}")


def clear_all_messages():
    try:
        subprocess.run(
            [sys.executable, "-m", "notion_cli.cli", "clear"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to clear all messages")


def delete_message():
    messages = get_all_messages()
    
    if not messages:
        print("No messages found in the database.")
        return

    print("\nAll Messages:")
    for i, msg in enumerate(messages, 1):
        print(f"{i}. From: {msg['sender']} | To: {msg['recipient']} | Message: {msg['message'][:30]}...")

    while True:
        try:
            choice = int(input("\nEnter the number of the message you want to delete (0 to cancel): "))
            if choice == 0:
                print("Deletion cancelled.")
                return
            if 1 <= choice <= len(messages):
                message_to_delete = messages[choice - 1]
                confirm = input(f"Are you sure you want to delete this message? (y/n)\n"
                                f"From: {message_to_delete['sender']}\n"
                                f"To: {message_to_delete['recipient']}\n"
                                f"Message: {message_to_delete['message']}\n")
                if confirm.lower() == 'y':
                    if notion_cli.notion_wrapper.delete_message(message_to_delete['ID']):
                        print(f"Message {choice} has been deleted.")
                    else:
                        print(f"Failed to delete message {choice}.")
                else:
                    print("Deletion cancelled.")
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("----------------------------")
    print("    Welcome to NotionMail!")
    while True:
        choice = print_menu()

        if choice == "send":
            send_message()
        elif choice == "read":
            read_messages()
        elif choice == "search":
            search_messages()
        elif choice == "delete":
            delete_message()
        elif choice == "clear":
            clear_all_messages()
        elif choice == "exit":
            print("\nGoodbye :D | Thanks for using NotionMail! - vivek")
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
