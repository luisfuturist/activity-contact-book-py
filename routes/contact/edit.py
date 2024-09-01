from utils.contact import get_contacts, save_contacts
from components.Contact import Contact

def ContactEdit(contact, dataIndex):
    Contact(contact)

    contacts = get_contacts()

    startedEditing = False

    def menu():
        if(startedEditing):
            action = input("\n[1] Name [2] Phone [3] Email [c] Cancel [s] Save\n:")

            if action == '1':
                new_name = input("Name: ")
                contact['name'] = new_name
            elif action == '2':
                new_phone = input("Phone: ")
                contact['phone'] = new_phone
            elif action == '3':
                new_email = input("Email: ")
                contact['email'] = new_email
            elif action == 's':
                contacts[dataIndex] = contact
                save_contacts(contacts)

                print("\nContact edited successfully\n")
                return
            elif action == 'c':
                return
            else:
                print("ERROR: Invalid option")

            menu()
        else:
            action = input("\n[1] Name [2] Phone [3] Email [c] Cancel\n:")

            if action == '1':
                new_name = input("Name: ")
                contact['name'] = new_name
            elif action == '2':
                new_phone = input("Phone: ")
                contact['phone'] = new_phone
            elif action == '3':
                new_email = input("Email: ")
                contact['email'] = new_email
            elif action == 'c':
                return
            else:
                print("ERROR: Invalid option")
            
            menu()
    menu()