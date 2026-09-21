contacts = {}


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully!")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Contact Book closed!")
        break

    else:
        print("Invalid choice! Try again.")

# concept: Dictionary contacts store karti hai → Add contact save karta hai → View contacts show karta hai → Search contact find karta hai → Update number change karta hai → Delete contact remove karta hai → while loop program ko running rakhta hai