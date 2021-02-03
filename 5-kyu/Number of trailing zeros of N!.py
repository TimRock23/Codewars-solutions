def zeros(x):
    i = 5
    count = 0
    while x >= i:
        count += x // i
        i *= 5
    return count
