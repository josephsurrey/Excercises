def calculate_average(absences):
    if not absences:
        return 0.0

    total_days = sum(absences)
    average_days = total_days / len(absences)
    return average_days


def find_person_with_most_absence(names, absences):
    if not absences:
        return "No data available"

    max_index = absences.index(max(absences))
    return names[max_index]


def find_people_not_absent(names, absences):
    if not absences:
        return "No data available"

    not_absent_names = [name for name, days in zip(names, absences) if days == 0]
    return sorted(not_absent_names)


def find_people_above_average(names, absences, average):
    if not absences:
        return "No data available"

    above_average_names = [name for name, days in zip(names, absences) if days > average]
    return sorted(above_average_names)


def main():
    names = []
    absences = []

    while True:
        input_str = input("Enter employee name and days absent (or $ to terminate): ")
        if input_str == '$':
            break

        try:
            name, days = input_str.rsplit(' ', 1)
            if not name or not days:
                print("Invalid input. Please provide both name and days absent.")
                continue

            absences.append(int(days))
            names.append(name)
        except ValueError:
            print("Invalid input. Days absent must be a valid integer.")
            continue

    if not absences:
        print("No data available. Exiting.")
        return

    average_days = calculate_average(absences)
    most_absent_person = find_person_with_most_absence(names, absences)
    not_absent_people = find_people_not_absent(names, absences)
    above_average_people = find_people_above_average(names, absences, average_days)

    print(f"\nAverage number of days staff were absent: {average_days:.2f}")
    print(f"Person with most days absent: {most_absent_person} with {max(absences)}")
    print(f"List of people not absent at all: {', '.join(not_absent_people)}")
    print(f"List of people absent above average: {', '.join(above_average_people)}")


main()
