import easygui as eg
import random

TITLE = "Yahtzee Lite"


def roll_dice():
    return sorted(random.randint(1, 6) for _ in range(5))


def welcome():
    eg.msgbox("Welcome to Yahtzee Lite\n"
              "Roll 5 dice (up to 3 times).\n"
              "Get all dice the same (Yahtzee!), 4 of a kind, or 3 of a kind to win! Good luck!", TITLE, "Play!")


def main():
    welcome()
    rolls_remaining = 2
    while True:
        dice = roll_dice()
        dice_text = f"You rolled: {' '.join(str(x) for x in dice)}"

        if dice.count(dice[0]) == 5:
            win_text = "\nYahtzee! You win!"
        elif any(dice.count(x) >= 3 for x in dice):
            kind = max(dice.count(x) for x in dice)
            win_text = f"\nCongratulations! You got {kind} of a kind!"
        else:
            win_text = ""

        if rolls_remaining > 0:
            remaining_text = f"\nRolls remaining: {rolls_remaining}"
            choices = ["Roll again", "Stick"]
        else:
            remaining_text = "\nOut of rolls!"
            choices = ["OK"]
            full_message = f"{dice_text}{win_text}{remaining_text}"
            roll_again = eg.buttonbox(full_message, TITLE, choices)
            break

        full_message = f"{dice_text}{win_text}{remaining_text}"
        roll_again = eg.buttonbox(full_message, TITLE, choices)

        if roll_again == "Stick":
            eg.msgbox(f"You chose to stick with {' '.join(str(x) for x in dice)}.", TITLE)
            break

        rolls_remaining -= 1
    play_again = eg.buttonbox("Would you like to play again?", TITLE, ["Yes", "No"])
    if play_again == "Yes":
        main()


main()
