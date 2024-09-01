from utils.contact import *
from routes.contact.index import ContactMain

def Header():
    print("-------------------------------------")
    print("Contact Book")
    print("-------------------------------------\n")
    
def Main():
    Header()
    ContactMain()

def main():
    save_default_contacts()
    load_contacts()

    while True:
        Main()

if __name__ == "__main__":
    main()
