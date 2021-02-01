import string


def is_pangram(s):
    letters = [_ for _ in string.ascii_lowercase]
    s = set(s.lower())
    for i in letters:
        if i not in s:
            return False
    return True
