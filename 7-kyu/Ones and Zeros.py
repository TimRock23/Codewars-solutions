def binary_array_to_number(arr):
    k = len(arr)
    result = 0
    for i in arr:
        k -= 1
        result += i*(2**k)
    return result
