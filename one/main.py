import itertools
def two_numbers(number_list):
    return next(c for c in itertools.combinations(number_list, 2) if sum(c) == 2020)

def three_numbers(number_list):
    return next(c for c in itertools.combinations(number_list, 3) if sum(c) == 2020)

