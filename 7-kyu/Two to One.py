def longest(s1, s2):
    arr = list(set(s1 + s2))
    sorted(arr)
    return ''.join(sorted(arr))
