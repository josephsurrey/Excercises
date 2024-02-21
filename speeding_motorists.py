WANTED_LIST = ["JAMES WILSON", "HELGA NORMAN", "ZACHARY CONROY"]


def calculate_fine(speed):
    if speed < 10:
        return 30
    elif 10 <= speed <= 14:
        return 80
    elif 15 <= speed <= 19:
        return 120
    elif 20 <= speed <= 24:
        return 170
    elif 25 <= speed <= 29:
        return 230
    elif 30 <= speed <= 34:
        return 300
    elif 35 <= speed <= 39:
        return 400
    elif 40 <= speed <= 44:
        return 510
    else:
        return 630


def process_speeder(name, speed):
    fine_amount = calculate_fine(speed)

    if name.upper() in WANTED_LIST:
        print(name.upper() + " - WARRANT TO ARREST")

    print(f"{name} to be fined ${fine_amount}")
    return {"Name": name, "Amount Over Limit": speed, "Fine Amount": fine_amount}


def display_summary(speeders):
    print("\nTotal fines:", len(speeders))
    total_fines = sum(speeder["Fine Amount"] for speeder in speeders)

    for i, speeder in enumerate(speeders, start=1):
        print(f"{i}) Name: {speeder['Name']} Amount Over Limit: {speeder['Amount Over Limit']}")

    print("\nTotal amount of fines: ${}".format(total_fines))


def main():
    speeders = []

    while True:
        name = input("Enter name of speeder: ")
        if name.lower() == "stop":
            break
        while True:
            try:
                speed = int(input("Enter the amount over speed limit: "))
                speeders.append(process_speeder(name, speed))
                break
            except ValueError:
                print("Please enter a valid number")

    display_summary(speeders)


main()
