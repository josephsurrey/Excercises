def display_menu():
    print("Welcome to MGS Childcare!")
    print("1. Check-in a child")
    print("2. Check-out a child")
    print("3. Calculate and print charges")
    print("4. Print the list of children")
    print("5. Exit")


def check_in(child_name, child_list):
    child_list.append(child_name)
    print(f"{child_name} has been checked in.")


def check_out(child_name, child_list):
    if child_name in child_list:
        child_list.remove(child_name)
        print(f"{child_name} has been checked out.")
    else:
        print(f"Error: {child_name} not found in the list.")


def calculate_charges(child_list, hours):
    charge_per_child = 12
    total_charge = len(child_list) * charge_per_child * hours
    print(f"Total charge for {len(child_list)} children for {hours} hours: ${total_charge}")


def print_child_list(child_list):
    print("Children currently checked in:")
    for child in child_list:
        print(child)


def main():
    child_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            child_name = input("Enter the name of the child to check in: ")
            check_in(child_name, child_list)
        elif choice == "2":
            child_name = input("Enter the name of the child to check out: ")
            check_out(child_name, child_list)
        elif choice == "3":
            hours = int(input("Enter the number of hours to charge: "))
            calculate_charges(child_list, hours)
        elif choice == "4":
            print_child_list(child_list)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()
