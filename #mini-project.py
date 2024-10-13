#mini-project

#Task 1: User Interface
#Task 2: Contact Data Storage
#Task 3: Menu Actions

print("Welcome to the Contact Management System!")

def menu():
    print("Menu")
    print("1. Add a new contact\n2. Edit an existing contact")
    print("3. Delete a contact\n4. Search for a contact")
    print("5. Display all contacts\n6. Export contacts to a text file")
    print("7. Quit")
    
menu()
option = input("Enter your option: ")
contact_info = {}


def add_contact():
    name = input("Enter full name: ").lower()
    number = input("Enter full number ((xxx)xxx-xxxx): ").lower()
    email = input("Enter email address: ").lower()
    contact_info[email] = {'Name': name, 'Phone Number': number, 'Email': email}
    print(contact_info)
  

def edit_contact(contact_info):
    print("Option 2 was chosen")
    unique_id = input("Which contact are you editing? (input email): ").lower()
    info = input("What information are you editing? (name/phone number/email): ").lower()
    if unique_id in contact_info:
        if info == "name":
            update_name = input("Enter update to user name: ").lower()
            contact_info[unique_id]['Name'] = update_name
        elif info == "phone number":
            update_number = input("Enter update to user phone number (xxx)xxx-xxxx: ").lower()
            contact_info[unique_id]['Phone Number'] = update_number
        elif info == "email":
            update_email = input("Enter update to user email: ").lower()
            contact_info[unique_id]['Email'] = update_email
    else:
        print("Email not in system")

def delete_contact():
    print("Option 3 has been chosen")
    contact_to_delete = input("Enter email of contact you want to delete: ").lower()
    if contact_to_delete in contact_info:
        contact_info.pop(contact_to_delete)
    else:
        print("That contact does not exist")

def search_contact():
    print("Option 4 has been chosen")
    searched_contact = input("Enter a contact email to search: ").lower()
    if searched_contact in contact_info:
        print(contact_info.setdefault(searched_contact))
    else:
        print("That contact does not exist")
               
def display_contact():
    print("Option 5 has been chosen")
    list_contacts = list(contact_info)
    print(list_contacts)

def export_contacts():
    with open('exported_contacts.txt', 'w') as file:
        for emails, details in contact_info.items():
            file.write(f'{emails}, {details}\n')



while True:
    if option == "1":
        add_contact()
        return_to_menu = input("Type 'exit' to go back to menu: ")
        if return_to_menu == "exit":
            menu()
            option = input("Enter your option: ")
    elif option == "2":
        edit_contact(contact_info)
        return_to_menu = input("Type 'exit' to go back to menu: ")
        if return_to_menu == "exit":
            menu()
            option = input("Enter your option: ")
    elif option == "3":
        delete_contact()
        return_to_menu = input("Type 'exit' to go back to menu: ")
        if return_to_menu == "exit":
            menu()
            option = input("Enter your option: ")
    elif option == "4":
        search_contact()
        return_to_menu = input("Type 'exit' to go back to menu: ")
        if return_to_menu == "exit":
            menu()
            option = input("Enter your option: ")
    elif option == "5":
        display_contact()
        return_to_menu = input("Type 'exit' to go back to menu: ")
        if return_to_menu == "exit":
            menu()
            option = input("Enter your option: ")
    elif option == "6":
        export_contacts()
        return_to_menu = input("Type 'exit' to go back to menu: ")
        if return_to_menu == "exit":
            menu()
            option = input("Enter your option: ")
    elif option == "7":
        print("Exiting System")
        break
    else:
        print("Option not valid")



