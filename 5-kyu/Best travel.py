from itertools import combinations


def choose_best_sum(t, k, ls):
    variants = combinations(ls, k)
    max_dist = 0
    for i in variants:
        if max_dist < sum(i) <= t:
            max_dist = sum(i)
    return max_dist if max_dist != 0 else None
