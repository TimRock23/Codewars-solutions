def nb_year(p0, percent, aug, p):
    n = 0
    while p0 < p:
        p0 += int(p0 * 0.01 * percent) + aug
        n += 1
    return n
