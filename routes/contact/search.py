from utils.contact import query_contact
from components.ContactList import ContactList
from routes.contact.details import ContactDetails

def ContactSearch():
    query = input("Enter the name, phone or email of the contact you are looking for: ")

    results, indices = query_contact(query)

    ContactList(results)

    def menu():
        if(len(results) == 0):
            action = input("[s] Query again [b] Back to main menu\n:")

            if action == 's':
                ContactSearch()
            elif action == 'b':
                return
            else:
                print("ERROR: Invalid option")
                menu()
        elif(len(results) == 1):
            action = input("[s] Query again [v] View contact [b] Back to main menu\n:")

            if action == 's':
                ContactSearch()
            elif action == 'v':
                ContactDetails(results[0], indices[0])
            elif action == 'b':
                return
            else:
                print("ERROR: Invalid option")
                menu()
        else:
            action = input("[s] Query again [<number>] View contact [b] Back to main menu\n:")

            if action.isdigit():
                i = int(action) - 1
                contact = results[i]
                ContactDetails(contact, indices[i])
            elif action == 's':
                ContactSearch()
            elif action == 'b':
                return
            else:
                print("ERROR: Invalid option")
    menu()
