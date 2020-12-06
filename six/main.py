import functools

def parse(filename):
    questions= []
    with open(filename) as f:
        lines = f.readlines()

    question_lines = []
    for line in lines:
        if line.strip() == "":
            questions.append(question_lines)
            question_lines = []
        else:
            question_lines.append(line.strip())
    if len(question_lines) > 0:
        questions.append(question_lines)

    return questions

def question_count(lines):
    return len(functools.reduce(lambda line_one, line_two: set(line_one) | set(line_two), lines ))

def question_union(lines):
    if len(lines) == 1:
        return len(lines[0])

    return len(functools.reduce(lambda line_one, line_two: set(line_one) & set(line_two), lines))
