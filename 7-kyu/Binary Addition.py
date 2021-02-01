def add_binary(a,b):
    num_ten = a + b
    res = ''
    while num_ten != 0:
        res += str(num_ten % 2)
        num_ten //= 2
    return res[::-1]
