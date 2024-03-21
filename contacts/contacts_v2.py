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
            print(f"ID: {contact['id']}\n"
                  f"Name: {contact['name']['first']} {contact['name']['last']}\n"
                  f"Mobile Number: {contact['mobile_number']}\n"
                  f"Email: {contact['email']}")
            return
    print(f"No contact with the ID '{id_number}' found.")


def print_contact_list(contact_list):
    for contact in contact_list:
        print(f"ID: {contact['id']}\n"
              f"Name: {contact['name']['first']} {contact['name']['last']}\n"
              f"Mobile Number: {contact['mobile_number']}\n"
              f"Email: {contact['email']}")


def search_contact(contact_list, search_name):
    found_ids = []
    for contact in contact_list:
        if (search_name.lower() in contact['name']['first'].lower()
                or search_name.lower() in contact['name']['last'].lower()):
            found_ids.append(contact['id'])
    return found_ids


def main():
    contact_list = []
    contact_1, contact_2 = test_contacts()

    contact_list.append(contact_1)
    contact_list.append(contact_2)

    while True:
        user_choice = input("Do you want to search for a specific contact (search) or print the full list (print)? "
                            "Enter 'quit' to exit: ")
        if user_choice.lower() == "search":
            search_name = input("Enter the name of the contact you want to search for: ")
            found_ids = search_contact(contact_list, search_name)
            if found_ids:
                for ids in found_ids:
                    print_contact(contact_list, id)
            else:
                print(f"No contact with the name '{search_name}' found.")
        elif user_choice.lower() == "print":
            print_contact_list(contact_list)
        elif user_choice.lower() == "quit":
            break
        else:
            print("Invalid choice. Please enter 'search', 'print', or 'quit'.")


main()
