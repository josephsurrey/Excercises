import easygui as eg
import random

TITLE = "Yahtzee Lite"


def roll_dice():
    return sorted(random.randint(1, 6) for _ in range(5))


def calculate_score(dice):
    if dice.count(dice[0]) == 5:
        return 50
    elif any(dice.count(x) >= 4 for x in dice):
        return 30
    elif any(dice.count(x) >= 3 for x in dice):
        return 10
    else:
        return 0


def get_player_name():
    return eg.enterbox("Enter your name:", TITLE)


def play_turn(player_name, rolls_remaining):
    dice = roll_dice()
    dice_text = f"You rolled: {' '.join(str(x) for x in dice)}"
    score = 0

    while True:
        if rolls_remaining > 0:
            remaining_text = f"\nRolls remaining: {rolls_remaining}"
            choices = ["Roll again", "Stick"]
        else:
            remaining_text = "\nOut of rolls!"
            choices = ["OK"]
            break

        full_message = f"{player_name}, {dice_text}\nScore: {score}{remaining_text}"
        roll_again = eg.buttonbox(full_message, TITLE, choices)

        if roll_again == "Stick":
            score = calculate_score(dice)
            eg.msgbox(f"{player_name}, you chose to stick with {score} points.", TITLE)
            break

        rolls_remaining -= 1
        dice = roll_dice()
        dice_text = f"You rolled: {' '.join(str(x) for x in dice)}"

    return score


def main():
    player1_name = get_player_name()
    player2_name = get_player_name()

    while True:
        player1_score = play_turn(player1_name, 2)
        player2_score = play_turn(player2_name, 2)

        if player1_score == player2_score:
            eg.msgbox(f"{player1_name} scored {player1_score} points.\n"
                      f"{player2_name} scored {player2_score} points.\n"
                      f"The game was tied", TITLE)
        elif player1_score > player2_score:
            eg.msgbox(f"{player1_name} scored {player1_score} points.\n"
                      f"{player2_name} scored {player2_score} points.\n"
                      f"{player1_name} wins!", TITLE)
        elif player1_score < player2_score:
            eg.msgbox(f"{player1_name} scored {player1_score} points.\n"
                      f"{player2_name} scored {player2_score} points.\n"
                      f"{player2_name} wins!", TITLE)

        play_again = eg.buttonbox("Would you like to play again?", TITLE, ["Yes", "No"])
        if play_again == "Yes":
            main()
        else:
            eg.msgbox("Thanks for playing Yahtzee")
            break


main()
