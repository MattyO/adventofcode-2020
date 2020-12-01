def two_numbers(number_list):
    for i, n in enumerate(number_list):
        for n2 in number_list[i:]:
            if n + n2 == 2020:
                return [n, n2]

def three_numbers(number_list):
    for i, n in enumerate(number_list):
        for j, n2 in enumerate(number_list[i:]):
            for n3 in number_list[j:]:
                if n + n2 + n3== 2020:
                    return [n, n2, n3]

