import string


def isspace(c):
    """returns 1 if the character is a space"""
    if (c == " "):
        return 1
    return 0


def ispunct(c):
    """returns 1 if the character is a punctuation marksk"""
    if (c in string.punctuation):
        return 1
    return 0


def analyze(text):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    length = len(text)
    upper = sum(letter.isupper() for letter in text)
    lower = sum(letter.islower() for letter in text)
    spaces = sum(letter.isspace() for letter in text)
    punctuation = sum(ispunct(letter) for letter in text)

    print('The text contains ' + str(length) + ' characters')
    print('- ' + str(upper) + ' upper letters')
    print('- ' + str(lower) + ' lower letters')
    print('- ' + str(punctuation) + ' punctuation marks')
    print('- ' + str(spaces) + ' spaces')


def text_analyzer(*multi_text):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if (len(multi_text) == 0):
        text = input("What is the text to analyse?\n")
        analyze(text)
    for text in multi_text:
        length = len(text)
        if (length == 0):
            text = input("What is the text to analyse?\n")
        analyze(text)
