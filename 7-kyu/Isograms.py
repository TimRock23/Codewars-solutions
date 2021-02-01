def is_isogram(string):
    s = string.lower()
    s_list = []
    for letter in s:
        if letter in s_list:
            return False
        else:
            s_list.append(letter)
    return True
