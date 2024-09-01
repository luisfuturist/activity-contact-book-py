import json
import os

contacts = []

def get_contacts():
    return contacts

def get_contact(ui_index):
    return contacts[ui_index - 1]

def load_contacts():
    global contacts

    try:
        with open('contacts.json', 'r') as file:
            loaded_contacts = json.load(file)
        
        is_list = isinstance(loaded_contacts, list)
        
        if not is_list:
            raise ValueError("JSON root element is not an array.")
        
        contacts = loaded_contacts
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit()

    except ValueError as e:
        print(f"Value error: {e}")
        exit()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()

def save_default_contacts():
    defaultContacts = []

    if not os.path.exists('contacts.json'):
        save_contacts(defaultContacts)

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def query_contact(query):
    query = query.lower()

    contacts = get_contacts()
    results = []
    indices = []

    for i, contact in enumerate(contacts):
        if query in contact['name'].lower() or query in contact['phone'].lower() or query in contact['email'].lower():
            results.append(contact)
            indices.append(i)

    return results, indices
