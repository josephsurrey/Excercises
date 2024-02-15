def silent_auction():
    item = input("What is the auction for? ")
    reserve_price = float(input("What is the reserve price? "))

    print(f"\nThe auction for the {item} has started!\n")

    highest_bid = 0

    while True:
        print(f"Highest bid so far is ${highest_bid}")

        bid_str = input("What is your bid? ")

        if bid_str.lower() == '-1':
            break

        try:
            bid = float(bid_str)

            if bid > highest_bid:
                highest_bid = bid
                print(f"Highest bid so far is ${highest_bid}\n")
            else:
                print("Please enter a higher bid\n")
        except ValueError:
            print("Invalid input. Please enter a valid bid or -1 to end the auction\n")

    if highest_bid >= reserve_price:
        print(f"\nThe auction for the {item} finished with a bid of ${highest_bid}")
    else:
        print(
            f"\nThe {item} didn't sell. The highest bid was ${highest_bid}, which did not meet the reserve price of ${reserve_price}")


silent_auction()
