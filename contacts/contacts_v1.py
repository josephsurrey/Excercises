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


def print_contact_list(contact_list):
    for contact in contact_list:
        print(f"ID: {contact['id']}\n"
              f"Name: {contact['name']['first']} {contact['name']['last']}\n"
              f"Mobile Number: {contact['mobile_number']}\n"
              f"Email: {contact['email']}")


def main():
    contact_list = []
    contact_1, contact_2 = test_contacts()

    contact_list.append(contact_1)
    contact_list.append(contact_2)

    print_contact_list(contact_list)


main()
