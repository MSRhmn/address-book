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
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            return []

    def save_contacts(self):
        """Dump the user input into corresponsing JSON file."""
        with open(self.filename, "w") as file:
            return json.dump(self.contacts, file, indent=4)

    def add_contact(self, first_name, last_name, phone_number, email=""):
        """Add new contact to the address book."""
        contact = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email,
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"\n Contact '{first_name} {last_name}' added successfully.")

    def search_contact(self, search_name):
        """Search for a contact by it's first name."""
        for contact in self.contacts:
            if search_name.lower() in contact["first_name"].lower():
                print(
                    f"\n Found contact: {contact['first_name']} {contact['last_name']}"
                )
                print(f" Phone: {contact['phone_number']}, Email: {contact['email']}")
                return
        print(f"\n No contact found for: '{search_name}'.")

    def delete_contact(self, first_name, last_name):
        """
        Delete a contact by searching it's first name and last name.
        If contact is found, it is removed and the file is saved.
        """
        found_contact = False
        for i, contact in enumerate(self.contacts):
            if (
                contact["first_name"].lower() == first_name.lower()
                and contact["last_name"].lower() == last_name.lower()
            ):
                del self.contacts[i]
                self.save_contacts()
                found_contact = True
                print(f"\n Contact '{first_name} {last_name}' deleted successfully.")
                break
        if not found_contact:
            print(f"\n No contact found with the name '{first_name} {last_name}'.")
