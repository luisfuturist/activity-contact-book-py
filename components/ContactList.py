def ContactList(contacts):
    if len(contacts) == 0:
        print("No contacts found")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. {contact['name']} - {contact['phone']} - {contact['email']}")

    print()
