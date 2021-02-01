def find_outlier(integers):
    odds = [i for i in integers if i % 2 == 1]
    evens = [i for i in integers if i % 2 == 0]
    return odds[0] if len(odds) == 1 else evens[0]
