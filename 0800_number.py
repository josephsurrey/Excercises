phone_letters = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7',
    'S': '7', 'T': '8', 'U': '8',
    'V': '8', 'W': '9', 'X': '9',
    'Y': '9', 'Z': '9'
}


def convert_to_number(user_word):
    number = ""
    word = user_word.upper()
    for letter in word:
        if letter in phone_letters:
            number += phone_letters[letter]

    return f"0800 {number}"


def main():
    number = convert_to_number(input("Enter a word to be converted to a 0800 phone number: "))
    print(number)


main()
