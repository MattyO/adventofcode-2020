def file_grouped_by_blanke_lines(filename):
    passports = []
    with open(filename) as f:
        contents = f.read()
        return [list(filter(lambda l: l != '', group.split('\n'))) for group in contents.split('\n\n')]
