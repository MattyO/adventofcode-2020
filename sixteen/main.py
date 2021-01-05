import collections
import lib.parser
import functools

RuleRange = collections.namedtuple("RuleRange", ['start', 'end'])

def parse(filename):
    rules = []
    ticket = None
    nearby_tickets = []

    groups = lib.parser.file_grouped_by_blanke_lines(filename)
    for rule_text in groups[0]:
        ranges = []
        name, range_text = rule_text.split(":")
        for single_range_text in range_text.split("or"):
            start, end = single_range_text.split('-')
            ranges.append(RuleRange(int(start.strip()) , int(end.strip())))

        rules.append(Rule(name, ranges))

    ticket = Ticket([ int(f) for f in groups[1][1].split(',')])

    for nearby_ticket in groups[2][1:]: 
        nearby_tickets.append(Ticket([ int(f) for f in nearby_ticket.split(',')]))



    return (rules, ticket, nearby_tickets)


class Ticket():
    def __init__(self, fields):
        self.fields = fields

    def invalid_fields(self, rules):
        return [ f for f in self.fields if not any(rule.is_valid(f) for rule in rules)]

    def field_labels(self, rules):
        labels =  []
        for field in self.fields:
            labels.append([rule.name for rule in rules if rule.is_valid(field)])

        return labels


class Rule:
    def __init__(self, name, rule_ranges):
        self.name = name
        self.rule_ranges = rule_ranges

    def is_valid(self, i):
        return any( r.start <= i <= r.end for r in self.rule_ranges)

    def __repr__(self):
        ranges_str_list = [ f"range({r.start}, {r.end})" for r in self.rule_ranges]
        return self.name + ": " + ", ".join(ranges_str_list)


def invalid(rules, tickets):
    return functools.reduce(lambda memo, ticket: memo + ticket.invalid_fields(rules), tickets, [])

def valid_tickets(rules, tickets):
    return [ticket for ticket in tickets if len(ticket.invalid_fields(rules)) == 0]

def possible_field_names(tickets, rules):
    field_names = { i: set(r.name for r in rules) for i in range(len(tickets[0].fields))}
    for tc, ticket in enumerate(tickets):
        for i, possible_field_names in enumerate(ticket.field_labels(rules)):
            field_names[i] &= set(possible_field_names) 

    possible_names = [ list(field_names[i]) for i in sorted(field_names.keys()) ]

    for i in range(len(possible_names)):
        ensured_names = set([possibilities[0] for possibilities in possible_names if len(possibilities) == 1])
        for i, possibilities in enumerate(possible_names):
            if len(possibilities) > 1:
                possible_names[i] = list(set(possibilities) - ensured_names)

    return [single_possibility[0] for single_possibility in possible_names]


