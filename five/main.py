import functools
def seat_id(pass_string):
    row_string = str(pass_string[:7])
    col_stirng = str(pass_string[7:])

    row_num = functools.reduce(lambda seats, c: seats[:int(len(seats)/2)] if c == 'F' else seats[int(len(seats)/2):], row_string , list(range(0,128)))[0]
    col_num  = functools.reduce(lambda seats, c: seats[:int(len(seats)/2)] if c == 'L' else seats[int(len(seats)/2):], col_stirng  , list(range(0,8)))[0]

    return (row_num, col_num, row_num * 8 + col_num)



