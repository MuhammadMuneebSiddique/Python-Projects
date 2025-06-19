
def add_contact(contact):

    print("\n --- ADD CONTACT NUMBER --- \n")

    name = input("Enter the Name: ")
    email = input("Enter the Email (optional): ")
    number = input("Enter the Number: ")

    if name and number:
        contact.append({"name":name,"email":email,"number":number})
    else:
        print("Error: Please enter the vaild information")

def view_contact(contact):
    print("\n --- VIEW CONTACT NUMBER --- \n")
    num = 0
    for items in contact:
        num += 1
        if not items["email"]:
            print(f"\n--- Contact Number {num} ---\n")
            print(f"Name: {items["name"]}")
            print(f"Contact Number: {items["number"]}")
            print()
        else:
            print(f"\n--- Contact Number {num} ---\n")
            print(f"Name: {items["name"]}")
            print(f"Email: {items["email"]}")
            print(f"Contact Number: {items["number"]}")
            print()

def search_contact(contact):
    print("\n --- SEARCH CONTACT NUMBER --- \n")
    search_number = input("Enter the name: ")
    for items in contact:
        if search_number.lower() == items["name"].lower():
            if not items["email"]:
                print()
                print(f"Name: {items["name"]}")
                print(f"Contact Number: {items["number"]}")
                print()
            else:
                print()
                print(f"Name: {items["name"]}")
                print(f"Email: {items["email"]}")
                print(f"Contact Number: {items["number"]}")
                print()

def delete_contact(contact):
    print("\n --- DELETE CONTACT NUMBER --- \n")
    delete_number = input("Enter the Number you can delete: ")

    for items in contact:
        if delete_number in [item["number"] for item in contact]:
            if delete_number == items["number"]:
                contact.remove(items)
                print("\n Number Delete Successfully \n")
        else:
            print("Number doesn't exist")


def contact_book():
    print("\n------ Welcome To Contact Book -----\n")

    contact = []
    while True:
        options = int(input("""1) Add Contact
2) View Contact
3) Search Contact
4) Delete Contact
5) Exit
Select the option: """))
        
        if options == 1:
            add_contact(contact)
        elif options == 2:
            view_contact(contact)
        elif options == 3:
            search_contact(contact)
        elif options == 4:
            delete_contact(contact)
        elif options == 5:
            break
    
contact_book()