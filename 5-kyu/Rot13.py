from string import ascii_lowercase as lower, ascii_uppercase as upper


def rot13(message):
    lowercase = str.maketrans(lower, lower[13:] + lower[:13])
    uppercase = str.maketrans(upper, upper[13:] + upper[:13])
    return message.translate(lowercase).translate(uppercase)
