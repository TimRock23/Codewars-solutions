def solution(number):
    arr = [i for i in range(number) if i % 3 == 0 or i % 5 == 0]
    return sum(arr)
