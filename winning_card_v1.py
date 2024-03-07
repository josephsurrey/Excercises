import random
import easygui as eg


CARD_NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
CARD_SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]


def draw_card():
    player_number = random.randint(0, 12)
    player_suit = random.randint(0, 3)
    com_number = random.randint(0, 12)
    com_suit = random.randint(0, 3)
    eg.msgbox(f"The computer's card was {CARD_NUMBERS[com_number]} of {CARD_SUITS[com_suit]}", "Winning Card Game")
    eg.msgbox(f"Your card was {CARD_NUMBERS[player_number]} of {CARD_SUITS[player_suit]}", "Winning Card Game")
    if player_number > com_number:
        eg.msgbox("You had the winning card!", "Winning Card Game")
    elif player_number < com_number:
        eg.msgbox("You had the losing card.", "Winning Card Game")
    else:
        eg.msgbox("Your cards tied", "Winning Card Game")


def main():
    play = eg.buttonbox("Do you want to play the card game?", "Winning Card Game", ["Yes", "No"])
    while True:
        if play == "Yes":
            draw_card()
            play = eg.buttonbox("Do you want to play again?", "Winning Card Game", ["Yes", "No"])
        else:
            break
    eg.msgbox("Thanks for playing Winning Card Game", "Winning Card Game", "Quit")


main()
