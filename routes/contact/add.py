from utils.contact import save_contacts, get_contacts

def ContactAdd():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }

    def menu():
        action = input("\n[c] Cancel [s] Save\n:")

        if action == 'c':
            return
        elif action == 's':
            contacts = get_contacts()
            contacts.append(contact)
            save_contacts(contacts)

            print("\nContact added successfully\n")
            return
        else:
            print("ERROR: Invalid option")
            menu()
    menu()
