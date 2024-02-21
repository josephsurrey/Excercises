def vehicle_list():
    return [
        {"Number": 1, "Type": "Suzuki Van", "Seats": 2},
        {"Number": 2, "Type": "Toyota Corolla", "Seats": 4},
        {"Number": 3, "Type": "Honda CRV", "Seats": 4},
        {"Number": 4, "Type": "Suzuki Swift", "Seats": 4},
        {"Number": 5, "Type": "Mitsubishi Airtrek", "Seats": 4},
        {"Number": 6, "Type": "Nissan DC Ute", "Seats": 4},
        {"Number": 7, "Type": "Toyota Previa", "Seats": 7},
        {"Number": 8, "Type": "Toyota Hi Ace", "Seats": 12},
        {"Number": 9, "Type": "Toyota Hi Ace", "Seats": 12},
    ]


def display_available_vehicles(vehicles, seats_needed):
    print("\nAvailable Vehicles:")
    print("Number\tType\t\tSeats")
    for vehicle in vehicles:
        print(f"{vehicle['Number']}\t{vehicle['Type']}\t{vehicle['Seats']}{' (Not enough seats)' if vehicle['Seats'] < seats_needed else ''}")


def book_vehicle(vehicles, booked_vehicles, seats_needed):
    vehicle_number = int(input("\nEnter the number of the vehicle to be booked (or -1 to stop booking mode): "))

    if vehicle_number == -1:
        print("\nBooking mode stopped. Thank you!")
        return

    selected_vehicle = next(
        (vehicle for vehicle in vehicles if vehicle["Number"] == vehicle_number and vehicle["Seats"] >= seats_needed),
        None)

    if selected_vehicle:
        person_name = input("Enter the name of the person booking the vehicle: ")
        booked_vehicles[selected_vehicle["Number"]] = {"Type": selected_vehicle["Type"], "Name": person_name}
        print(f"\nVehicle {selected_vehicle['Number']} ({selected_vehicle['Type']}) booked for {person_name}.\n")
    else:
        print(f"\nInvalid selection. Please choose an available vehicle with enough seats.\n")


def display_booked_vehicles(booked_vehicles):
    print("\nEnd of the Day - Booked Vehicles:\n")
    print("Number\tType\t\tName")
    for number, booking_info in booked_vehicles.items():
        print(f"{number}\t{booking_info['Type']}\t{booking_info['Name']}")


def main():
    vehicles = vehicle_list()
    booked_vehicles = {}

    print("Vehicle Booking System - Start of the Day\n")

    while True:
        seats_needed = int(input("Enter the number of seats needed (or -1 to stop): "))

        if seats_needed == -1:
            print("\nBooking mode stopped. Thank you!")
            break

        display_available_vehicles(vehicles, seats_needed)
        book_vehicle(vehicles, booked_vehicles, seats_needed)

    display_booked_vehicles(booked_vehicles)


main()
