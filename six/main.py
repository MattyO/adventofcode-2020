import functools
import lib.parser

def parse(filename):
    return lib.parser.file_grouped_by_blanke_lines(filename)

def question_count(lines):
    return len(functools.reduce(lambda line_one, line_two: set(line_one) | set(line_two), lines ))

def question_union(lines):
    if len(lines) == 1:
        return len(lines[0])

    return len(functools.reduce(lambda line_one, line_two: set(line_one) & set(line_two), lines))
