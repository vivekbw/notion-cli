# Interview question was to implement a text document class that could handle:

# applying an operation(the two operations are inserting text the end of the document and deleting n characters from the end of the document)
# undoing the latest operation
# redoing the latest operation
# get the current content
# Don't expect any hints during the interview


class TextDocument:
    def __init__(self):
        self.content = ""
        self.history = []
        self.future = []

    def insert(self, text):
        self.history.append(('insert', len(text)))
        self.content += text
        self.future.clear()

    def delete(self, n):
        deleted_text = self.content[-n:]
        self.history.append(('delete', deleted_text))
        self.content = self.content[:-n]
        self.future.clear()

    def undo(self):
        if not self.history:
            print("Nothing to undo.")
            return

        last_action, data = self.history.pop()

        if last_action == 'insert':
            self.future.append(('insert', self.content[-data:]))
            self.content = self.content[:-data]
        elif last_action == 'delete':
            self.future.append(('delete', len(data)))
            self.content += data

    def redo(self):
        if not self.future:
            print("Nothing to redo.")
            return

        next_action, data = self.future.pop()

        if next_action == 'insert':
            self.content += data
            self.history.append(('insert', len(data)))
        elif next_action == 'delete':
            deleted_text = self.content[-data:]
            self.content = self.content[:-data]
            self.history.append(('delete', deleted_text))

    def get_content(self):
        if len(self.content) == 0:
            return "No content"
        return self.content


def main():
    doc = TextDocument()
    print("Text Document Editor")
    print("Commands: insert <text>, delete <n>, undo, redo, content, exit")

    while True:
        command = input("\nEnter command: ").strip().split(maxsplit=1)

        if not command:
            continue

        action = command[0].lower()

        if action == "insert":
            if len(command) > 1:
                doc.insert(command[1])
            else:
                print("\nPlease provide text to insert.")
        elif action == "delete":
            if len(command) > 1 and command[1].isdigit():
                doc.delete(int(command[1]))
            else:
                print("\nPlease provide the number of characters to delete.")
        elif action == "undo":
            doc.undo()
        elif action == "redo":
            doc.redo()
        elif action == "content":
            print("\nCurrent content:\n", doc.get_content())
        elif action == "exit":
            break
        else:
            print("\nUnknown command.")


if __name__ == "__main__":
    main()
