def divisors(integer):
    result = []
    for i in range(2, integer//2 + 1):
        if integer % i == 0:
            result.append(i)
    return result if len(result) else f'{integer} is prime'
