import easygui as eg
import random


def welcome():
    play = eg.buttonbox("Welcome to Rock Paper Scissors.\n"
                        "Rock beats scissors\n"
                        "Paper beats rock\n"
                        "Scissors beats paper\n"
                        "\n"
                        "Do you want to play?", "Paper, Scissors, Rock", ["Yes", "No"])
    return play


def weapon_choice():
    weapon = eg.buttonbox("Choose your weapon", "Paper, Scissors, Rock", ["Paper", "Scissors", "Rock"])
    com_weapon = random.choice(["Paper", "Scissors", "Rock"])
    return weapon, com_weapon


def fight(player_weapon, computer_weapon):
    if player_weapon == computer_weapon:
        return f"Draw! You both chose {player_weapon}"

    elif player_weapon == "Rock":
        if computer_weapon == "Scissors":
            return f"You win! {player_weapon} beats {computer_weapon}"
        else:
            return f"Computer wins! {computer_weapon} beats {player_weapon}"

    elif player_weapon == "Paper":
        if computer_weapon == "Rock":
            return f"You win! {player_weapon} beats {computer_weapon}"
        else:
            return f"Computer wins! {computer_weapon} beats {player_weapon}"

    elif player_weapon == "Scissors":
        if computer_weapon == "Paper":
            return f"You win! {player_weapon} beats {computer_weapon}"
        else:
            return f"Computer wins! {computer_weapon} beats {player_weapon}"


def main():
    while True:
        play = welcome()
        if play == "Yes":
            weapon = weapon_choice()
        else:
            eg.msgbox("Goodbye!", "Paper, Scissors, Rock")
            break
        result = fight(weapon[0], weapon[1])
        eg.msgbox(result)


main()
