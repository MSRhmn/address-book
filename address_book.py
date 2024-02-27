import json
from pathlib import Path


class AddressBook:
    """A simple attempt to represent a address book."""

    def __init__(self, filename):
        self.filename = filename
        self.file_path = Path(filename)
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """
        Load contacts from the JSON file.
        If the file doesn't exist or cannot be read, return an empty list.
        """
        if self.file_path.exists():
            contents = self.file_path.read_text()
            return json.loads(contents)
        else:
            return []


address_book = AddressBook("contacts.json")
print(address_book.load_contacts())
