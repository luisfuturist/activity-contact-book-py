from utils.contact import save_contacts, get_contacts
from components.Modal import Modal

def ContactDeleteModal(index):
    Modal("Delete contact", [
        "Are you sure you want to delete this contact?",
        "This action cannot be undone"
    ])

    def menu():
        action = input("\n[c] Cancel [y] Confirm\n:")

        if action == 'c':
            return
        elif action == 'y':
            contacts = get_contacts()
            contacts.pop(index)
            save_contacts(contacts)

            print("\nContact deleted successfully\n")
            return
        else:
            print("ERROR: Invalid option")
            menu()
    menu()
