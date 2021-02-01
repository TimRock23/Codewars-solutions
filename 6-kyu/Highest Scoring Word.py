import string


LETTERS = {i: n for n, i in enumerate(string.ascii_lowercase)}


def high(x):
    words = x.split()
    max_cost = 0
    biggest = ''
    for word in words:
        word_cost = 0
        for letter in word:
            word_cost += LETTERS[letter]
        if word_cost > max_cost:
            max_cost = word_cost
            biggest = word
    return biggest
