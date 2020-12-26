import functools

def find_combination(ids_and_offsets):
    def product(ids):
        return functools.reduce(lambda x,y: x*y, ids)

    accumed_ids = []
    offset, multiplier = ids_and_offsets.pop(0)
    accumed_ids.append(multiplier)
    intersetion = multiplier

    while len(ids_and_offsets) > 0:
        index = 1
        next_offset, next_id = ids_and_offsets.pop(0)
        top = 10000
        temp = 0
        while temp <= product(accumed_ids) * next_id:
            temp = (multiplier * index) + offset
            #(6834 -2) / 13
            if (temp + next_offset) % next_id == 0:
                accumed_ids.append(next_id)
                intersetion = temp
                multiplier = product(accumed_ids)
                offset = temp - multiplier
                break

            index += 1

    return intersetion

def find_departure(starting_point, bus_ids):
    bus_ids = [ bus_id for bus_id in bus_ids if bus_id is not None ]
    max_ending = starting_point + min(bus_ids)
    next_bus_info = None

    for i in range(starting_point, max_ending):
        matching_ids = [ bus_id  for bus_id in bus_ids if i % bus_id == 0 ]
        if any( iter(matching_ids) ):
            next_bus_info  = (i, next(iter(matching_ids)))
            break;

    return next_bus_info

