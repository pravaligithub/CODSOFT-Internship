class contact:
    def __init__(self, name, phonenum, email, address):
        self.name = name
        self.phonenum = phonenum
        self.email = email
        self.address = address
class AddressBook:
    def __init__(self):
        self.contacts=[]
    def add_contact(self, contact):
        self.contacts.append(contact)
    def view_contacts(self):
        if not self.contacts:
            print(" No contacts found ")
            return
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}.Name:{contact.name},phone:{contact.phonenum}")
    def search_contacts(self,search_term):
        found_contacts=[]
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phonenum:
                found_contacts.append(contact)
            return found_contacts
    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact
    def delete_contact(self, index):
        del self.contacts[index]

def main():
    address_book = AddressBook()
    while True:
        print("\n-- Address Book Menu--")
        print("1. Add contact")
        print("2. view contact")
        print("3. search contact")
        print("4. update contact")
        print("5. delete contact")
        print("6. Quit")


        choice = input(" Enter your choice(1-6): ")

        if choice == '1':
            name = input(" Enter name: ")
            phonenum = input("Enter phonenum:")
            email = input("Enter email address")
            address = input(" Enter address: ")
            new_contact=contact(name, phonenum, email, address)
            address_book.add_contact(new_contact)

        elif choice == '2':
            address_book.view_contacts()

        elif choice == '3':
            search_term = input("enter name or phonenum to search:")
            found_contacts = address_book.search_contacts(Search_term)
            if not found_contacts:
                print("no matching contacts found:")
            else:
                print("matching contacts:")
                for i,contacts in enumerate(found_contacts):
                    print(f"{i+1},Name:{contact.name},phone:{contact.phone}")

        elif choice == '4':
            index = int(input("enter the index of the contact you want to update:"))
            if index >= 0  and index < len(address_book.contacts):
               address_book.delete_contact(index)
               print("contact deleted successfully")
            else:
                print("invalid index")
        elif choice == '6':
             break

        else:
            print("invalid choice.")
if __name__ == "__main__":
    main()


