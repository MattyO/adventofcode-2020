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
            list_to_sum = item_list[i:counter]
            the_sum = sum(item_list[i:counter])

            if the_sum > num:
                continue
            elif the_sum == num:
                return list_to_sum

    return None




