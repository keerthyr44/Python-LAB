contact_book = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add or Update Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name in contact_book:
            print(f"Updating {name}'s number from {contact_book[name]} to {phone}.")
        else:
            print(f"Adding new contact: {name} - {phone}")

        contact_book[name] = phone

    elif choice == '2':
        if not contact_book:
            print("Contact book is empty.")
        else:
            print("\nAll Contacts:")
            for name, number in contact_book.items():
                print(f"{name}: {number}")

    elif choice == '3':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
