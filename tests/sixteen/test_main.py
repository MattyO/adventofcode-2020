import unittest
import sixteen.main
from sixteen.main import Ticket, RuleRange, Rule

class ParseTest(unittest.TestCase):

    def test_parse(self):
        rules, ticket, nearby_tickets = sixteen.main.parse('sixteen/example.txt')

        self.assertEqual(len(rules), 3) 
        self.assertEqual(rules[0].name, 'class') 
        self.assertEqual(rules[0].rule_range[0].start, 1) 
        self.assertEqual(rules[0].rule_range[0].end, 3) 

        self.assertEqual(len(ticket.fields), 3) 
        self.assertEqual(ticket.fields, [7, 1, 14]) 

        self.assertEqual(len(nearby_tickets), 4) 
        self.assertEqual(nearby_tickets[0].fields, [7,3,47]) 

class TicketTest(unittest.TestCase):

    def test_is_valid_true(self):
        ticket = Ticket([7,3,47])
        rules = [
            Rule('class', [RuleRange(1,3), RuleRange(5,7)]),
            Rule('row', [RuleRange(6,11), RuleRange(33,44)]),
            Rule('seat', [RuleRange(13,40), RuleRange(45,50)]),
        ]

        self.assertEqual(ticket.invalid_fields(rules), [])

    def test_is_valid_false(self):
        ticket = Ticket([40,4,50])
        rules = [
            Rule('class', [RuleRange(1,3), RuleRange(5,7)]),
            Rule('row', [RuleRange(6,11), RuleRange(33,44)]),
            Rule('seat', [RuleRange(13,40), RuleRange(45,50)]),
        ]

        self.assertEqual(ticket.invalid_fields(rules), [4])


class InvalidTest(unittest.TestCase):
    def test_exmaple(self):
        rules, ticket, nearby_tickets = sixteen.main.parse('sixteen/example.txt')
        self.assertEqual(
            sorted(sixteen.main.invalid(rules, nearby_tickets)), 
            sorted([4 , 55 , 12])
        )
        self.assertEqual(sum(sixteen.main.invalid(rules, nearby_tickets)), 71)

    def test_puzzle(self):
        rules, ticket, nearby_tickets = sixteen.main.parse('sixteen/puzzle.txt')
        self.assertEqual(sum(sixteen.main.invalid(rules, nearby_tickets)), 71)


