from utils.contact import get_contacts, get_contact
from components.ContactList import ContactList
from routes.contact.details import ContactDetails
from routes.contact.add import ContactAdd
from routes.contact.search import ContactSearch

def ContactMain():
    contacts = get_contacts()
    ContactList(contacts)

    def menu():
        if(len(contacts) == 0):
            action = input("[a] Add a contact [e] Exit application\n:")
            
            if action == 'a':
                ContactAdd()
            elif action == 'e':
                exit()
            else:
                print("\nERROR: Invalid option\n")
        elif (len(contacts) == 1):
            action = input("[a] Add a contact [v] View the contact [e] Exit application\n:")
            
            if action == 'a':
                ContactAdd()
            elif action == 'v':
                ContactDetails(contacts[0], 0)
            elif action == 'e':
                exit()
            else:
                print("\nERROR: Invalid option\n")
        else:
            action = input("[a] Add a contact [s] Search for a contact [<number>] View the contact [e] Exit application\n:")
            
            if action.isdigit():
                i = int(action)
                contact = get_contact(i)
                ContactDetails(contact, i - 1)
            elif action == 'a':
                ContactAdd()
            elif action == 's':
                ContactSearch()
            elif action == 'e':
                exit()
            else:
                print("\nERROR: Invalid option\n")
    menu()
