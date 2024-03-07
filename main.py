from address_book import AddressBook


def main():
    address_book = AddressBook("contacts.json")

    while True:
        print("\nAddress Book Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            address_book.add_contact(first_name, last_name, phone_number, email)
        elif choice == "2":
            search_name = input("Enter first name to search: ")
            address_book.search_contact(search_name)
        elif choice == "3":
            first_name = input("Enter first name of the contact to delete: ")
            last_name = input("Enter last name of the contact to delete: ")
            address_book.delete_contact(first_name, last_name)
        elif choice == "4":
            print("Exiting address book..")
            break
        else:
            print("Invalid choice. Please select '1, 2, 3 or 4'.")


if __name__ == "__main__":
    main()
