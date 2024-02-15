def start_trip(total_time, total_income, total_trips):
    try:
        trip_time = float(input("Enter the time the trip took in minutes: "))
        if trip_time < 0:
            print("Trip time cannot be negative. Please enter a valid value.")
            return total_time, total_income, total_trips
        else:
            base_cost = 10
            cost_per_minute = 2
            trip_cost = base_cost + (cost_per_minute * trip_time)

            total_time += trip_time
            total_income += trip_cost
            total_trips += 1

            print(f"Trip details - Time: {trip_time} minutes, Cost: ${trip_cost:.2f}")
            return total_time, total_income, total_trips
    except ValueError:
        print("Invalid input. Please enter a valid number for trip time.")
        return total_time, total_income, total_trips


def print_summary(driver_name, total_time, total_income, total_trips):
    if total_trips == 0:
        print("No trips taken today.")
        return

    average_time = total_time / total_trips
    average_cost = total_income / total_trips

    print("\nSummary:")
    print(f"Driver's name: {driver_name}")
    print(f"Total time of all trips: {total_time} minutes")
    print(f"Average time of all trips: {average_time:.2f} minutes")
    print(f"Total income for the day: ${total_income:.2f}")
    print(f"Average cost of all trips: ${average_cost:.2f}")


def main():
    driver_name = input("Enter the driver's name: ")
    total_time = 0
    total_income = 0
    total_trips = 0

    while True:
        start_trip_input = input("Start a new trip? (yes/no): ").lower()

        if start_trip_input == "yes":
            total_time, total_income, total_trips = start_trip(total_time, total_income, total_trips)
        elif start_trip_input == "no":
            print_summary(driver_name, total_time, total_income, total_trips)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


main()
