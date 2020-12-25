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

