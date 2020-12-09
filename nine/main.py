import itertools

def is_valid(num, num_range):
    return any([combo for combo in itertools.combinations(num_range, 2) if sum(combo) == num])


def is_valid_window(item_list, window_size):
    for i, item in enumerate(item_list[window_size:]):
        if not is_valid(item, item_list[i:i+window_size]):
            return item
    return None

def contiguous_set(item_list, num):
    for i, item in enumerate(item_list):
        for counter in range(i, len(item_list)):
            sum_list = item_list[i:counter]
            if sum(sum_list) > num:
                continue
            elif sum(sum_list) == num:
                return sum_list

    return None




