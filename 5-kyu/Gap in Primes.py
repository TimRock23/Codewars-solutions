def is_prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


def gap(g, m, n):
    prev_prime = n
    for i in range(m, n+1):
        if is_prime(i):
            if i - prev_prime == g:
                return [prev_prime, i]
            else:
                prev_prime = i
    return None
