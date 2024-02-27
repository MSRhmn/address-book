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

    def add_contact(self, first_name, last_name, phone_number, email):
        """Add new contact to the address book."""
        contact = {
            "firs_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email,
        }
        self.contacts.append(contact)
        self.save_contacts()

    def save_contacts(self):
        """
        Dump user input into JSON string.
        Write out the JSON string to the address book JSON file.
        """
        contents = json.dumps(self.contacts)
        self.file_path.write_text(contents)


# address_book = AddressBook("contacts.json")
# print(address_book.load_contacts())
