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


class Rule:
    def __init__(self, name, rule_ranges):
        self.name = name
        self.rule_ranges = rule_ranges

    def is_valid(self, i):
        return any( r.start <= i <= r.end for r in self.rule_ranges)


def invalid(rules, tickets):
    return functools.reduce(lambda memo, ticket: memo + ticket.invalid_fields(rules), tickets, [])
