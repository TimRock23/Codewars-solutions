def get_count(input_str):
    num_vowels = 0
    letters = ['a', 'e', 'i', 'o', 'u']
    for i in input_str:
        if i in letters:
            num_vowels += 1
    return num_vowels
