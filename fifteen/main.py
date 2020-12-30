def item_at(starting_list, length):
    start_list_length = len(starting_list)
    last_list_item = None

    last_index_map = { k: starting_list.index(k) + 1 for k in starting_list }

    for i in range(start_list_length + 1, length + 1 ):
        next_list_item = 0
        last_list_item_index = i - 1

        if last_list_item in last_index_map.keys():
            next_list_item = last_list_item_index  - last_index_map[last_list_item]
            last_index_map[last_list_item] = last_list_item_index 
        else: 
            last_index_map[last_list_item] = last_list_item_index

        last_list_item = next_list_item

    return last_list_item
