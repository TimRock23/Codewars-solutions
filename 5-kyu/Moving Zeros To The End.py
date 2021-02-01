def move_zeros(array):
    zeroes = []
    arr = []
    for i in array:
        if i == 0 and type(i) != bool:
            zeroes.append(i)
        else:
            arr.append(i)
    arr += zeroes
    return arr
