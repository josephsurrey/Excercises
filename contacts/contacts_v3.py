import easygui as eg

TITLE = "Contact List"


def create_contact(id_number, first_name, last_name, mobile_number, email):
    contact = {
        "id": id_number,
        "name": {
            "first": first_name,
            "last": last_name
        },
        "mobile_number": mobile_number,
        "email": email
    }
    return contact


def test_contacts():
    contact_1 = create_contact(1, "John", "Matua", "027 121 1245",
                               "matua_j@maxmail.com")
    contact_2 = create_contact(2, "Smith", "Pearson", "029 127 1247",
                               "selat@maxmail.co.lt")
    return contact_1, contact_2


def print_contact(contact_list, id_number):
    for contact in contact_list:
        if contact['id'] == id_number:
            eg.msgbox(f"ID: {contact['id']}\n"
                      f"Name: {contact['name']['first']} {contact['name']['last']}\n"
                      f"Mobile Number: {contact['mobile_number']}\n"
                      f"Email: {contact['email']}", TITLE)
            return
    eg.msgbox(f"No contact with the ID '{id_number}' found.", "Contact Not Found")


def print_contact_list(contact_list):
    contact_info = ""
    for contact in contact_list:
        contact_info += f"ID: {contact['id']}\n" \
                        f"Name: {contact['name']['first']} {contact['name']['last']}\n" \
                        f"Mobile Number: {contact['mobile_number']}\n" \
                        f"Email: {contact['email']}\n\n"
    eg.msgbox(contact_info, TITLE)


def search_contact(contact_list, search_name):
    found_ids = []
    for contact in contact_list:
        if (search_name.lower() in contact['name']['first'].lower()
                or search_name.lower() in contact['name']['last'].lower()):
            found_ids.append(contact['id'])
    return found_ids


def add_contact(contact_list):
    id_number = len(contact_list) + 1
    first_name = eg.enterbox("Enter the first name:", TITLE)
    last_name = eg.enterbox("Enter the last name:", TITLE)
    mobile_number = eg.enterbox("Enter the mobile number:", TITLE)
    email = eg.enterbox("Enter the email:", TITLE)
    new_contact = create_contact(id_number, first_name, last_name, mobile_number, email)
    contact_list.append(new_contact)
    eg.msgbox("Contact added successfully!", TITLE)


def main():
    contact_list = []
    contact_1, contact_2 = test_contacts()
    contact_list.append(contact_1)
    contact_list.append(contact_2)

    while True:
        user_choice = eg.buttonbox("Do you want to search for a specific contact, add a contact, or print the full "
                                   "list?", TITLE, ["Search", "Add", "Print", "Quit"])
        if user_choice == "Search":
            search_name = eg.enterbox("Enter the name of the contact you want to search for:", TITLE)
            found_ids = search_contact(contact_list, search_name)
            if found_ids:
                for id_number in found_ids:
                    print_contact(contact_list, id_number)
            else:
                eg.msgbox(f"No contact with the name '{search_name}' found.", "Contact Not Found")
        elif user_choice == "Add":
            add_contact(contact_list)
        elif user_choice == "Print":
            print_contact_list(contact_list)
        elif user_choice == "Quit":
            break


main()
