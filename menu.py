"""
Menu for the NotionMail CLI
"""
import subprocess
import sys
from datetime import datetime


def print_menu():
    print("----------------------------")
    print("\nMenu:")
    print("Type 'send' to send a message")
    print("Type 'read' to read messages")
    print("Type 'search' to search for a message")
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


def main():
    print("----------------------------")
    print("    Welcome to NotionMail!")
    while True:
        choice = print_menu()

        if choice == "send":
            send_message()
        elif choice == "read":
            read_messages()
        elif choice == "exit":
            print("\nGoodbye :D | Thanks for using NotionMail! - vivek")
            sys.exit()
        elif choice == "search":
            search_messages()
        elif choice == "clear":
            clear_all_messages()
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
