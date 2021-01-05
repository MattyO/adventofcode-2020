import functools
import unittest
import sixteen.main
from sixteen.main import Ticket, RuleRange, Rule, valid_tickets, possible_field_names

class ParseTest(unittest.TestCase):

    def test_parse(self):
        rules, ticket, nearby_tickets = sixteen.main.parse('sixteen/example.txt')

        self.assertEqual(len(rules), 3) 
        self.assertEqual(rules[0].name, 'class') 
        self.assertEqual(rules[0].rule_ranges[0].start, 1) 
        self.assertEqual(rules[0].rule_ranges[0].end, 3) 

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

    def test_field_labels(self):
        ticket = Ticket([7,1,14])
        rules = [
            Rule('class', [RuleRange(1,3), RuleRange(5,7)]),
            Rule('row', [RuleRange(6,11), RuleRange(33,44)]),
            Rule('seat', [RuleRange(13,40), RuleRange(45,50)]),
        ]

        self.assertEqual(
            ticket.field_labels(rules),
            [['class', 'row',], ['class'], ['seat']]

        )



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
        self.assertEqual(sum(sixteen.main.invalid(rules, nearby_tickets)), 20231)

class ValidTicketsTest(unittest.TestCase):
    def test_valid_tickets(self):
        rules, ticket, nearby_tickets = sixteen.main.parse('sixteen/puzzle.txt')

        self.assertEqual(
            len(valid_tickets(rules, nearby_tickets)), 
            190
        )

class PossibleTicketNamesTest(unittest.TestCase):
    def test_example(self):
        rules, ticket, nearby_tickets = sixteen.main.parse('sixteen/example2.txt')
        self.assertEqual(
            possible_field_names(nearby_tickets, rules),
            ['row', 'class', 'seat']
        )

    def test_puzzle(self):
        rules, ticket, nearby_tickets = sixteen.main.parse('sixteen/puzzle.txt')
        possible_nearby_tickets = valid_tickets(rules, nearby_tickets)
        possible_field_name_list = possible_field_names(possible_nearby_tickets, rules)
        self.assertEqual(
            possible_field_name_list,
            [
                'type',
                'arrival platform',
                'arrival location',
                'class',
                'departure date',
                'departure station',
                'departure track',
                'arrival track',
                'train',
                'zone',
                'route',
                'row',
                'price',
                'duration',
                'wagon',
                'departure platform',
                'arrival station',
                'departure location',
                'departure time',
                'seat',
            ])

        departure_indexes = { i: n for i, n in enumerate(possible_field_name_list) }
        departure_values = { k: ticket.fields[i] for i, k in departure_indexes.items() if k.startswith("departure") } 
        departure_product = functools.reduce(lambda x, y: x * y, departure_values.values())

        self.assertEqual(departure_product, 1940065747861)



