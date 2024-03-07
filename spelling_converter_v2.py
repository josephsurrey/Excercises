import easygui as eg


def get_word():
    word = eg.enterbox("Enter a word to be converted to US spelling:", "Spelling Converter V2")
    return word


def convert_to_us(word):
    word_list = list(word)
    if "our" in word:
        del word_list[word.find("u")]
    elif "ise" in word or "yse" in word:
        i = word.find("i")
        word_list[i + 1] = "z"
    elif "yse" in word:
        i = word.find("y")
        word_list[i + 1] = "z"
    return "".join(word_list)


def main():
    while True:
        