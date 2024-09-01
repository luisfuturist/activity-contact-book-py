from modals.ContactDeleteModal import ContactDeleteModal
from routes.contact.edit import ContactEdit
from components.Contact import Contact

def ContactDetails(contact, dataIndex):
    Contact(contact)

    action = input("[e] Edit contact [d] Delete contact [b] Back to main menu\n:")

    if action == 'e':
        ContactEdit(contact, dataIndex)
    elif action == 'd':
        ContactDeleteModal(dataIndex)
    elif action == 'b':
        return
    else:
        print("ERROR: Invalid option")
        ContactDetails(contact, dataIndex)
