import functools

def search(char_list, front_char, range_size):
    return functools.reduce(lambda seats, c: seats[:int(len(seats)/2)] if c == front_char else seats[int(len(seats)/2):], char_list , list(range(0,range_size)))[0]

def seat_id(pass_string):
    row_string = str(pass_string[:7])
    col_string = str(pass_string[7:])

    row_num = search(row_string, 'F', 128)
    col_num = search(col_string  , 'L', 8)

    return (row_num, col_num, row_num * 8 + col_num)



