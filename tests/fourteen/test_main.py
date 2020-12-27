import unittest
import unittest.mock
import fourteen.main
from lib.computer import Instruction


class MaskTest(unittest.TestCase):

    def test_mask(self):
        test_value   = "000000000000000000000000000000001011"
        test_mask    = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        expect_value = '000000000000000000000000000001001001'

        self.assertEqual(
            fourteen.main.mask(test_value, test_mask),
            expect_value
        )

    def test_mask_2(self):
        test_value   = "000000000000000000000000000001100101"
        test_mask    = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        expect_value = '000000000000000000000000000001100101'

        self.assertEqual(
            fourteen.main.mask(test_value, test_mask),
            expect_value
        )

    def test_mask_3(self):
        test_value   = "000000000000000000000000000000000000"
        test_mask    = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        expect_value = '000000000000000000000000000001000000'

        self.assertEqual(
            fourteen.main.mask(test_value, test_mask),
            expect_value
        )


class ParseTest(unittest.TestCase):

    def test_parse_example(self):
        instructions = fourteen.main.parse('fourteen/example.txt')

        self.assertEqual(len(instructions), 4)
        self.assertIsInstance(instructions[0], Instruction)

        self.assertEqual(instructions[0].operation, 'mask')
        self.assertEqual(
            instructions[0].argument,
            'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        )

        self.assertEqual(instructions[1].operation, 'mem')
        self.assertEqual(
            instructions[1].argument, 
            (8, 11)
        )

        self.assertEqual(instructions[2].operation, 'mem')


class DockingInstructionSetTest(unittest.TestCase):

    def test_address_sum(self):
        dc_mock = unittest.mock.Mock(world={
            'memory': {8: 20, 23: 10},
            'mask': None,
            })

        self.assertEqual(fourteen.main.address_sum(dc_mock), 30)

    def test_mask(self):
        starting_world = {'mask': None}
        mask_instruction = Instruction('mask', "XXX01X1")
        self.assertEqual(
            fourteen.main.DockingInstructionSet().mask(mask_instruction, starting_world),
            {'mask': 'XXX01X1'}
        )

    def test_mem(self):
        starting_world = {
                'memory': {},
                'mask': "1XXXX0X".rjust(36, "X")
                }
        mem_instruction = Instruction('mem', (8, 11))

        new_world = fourteen.main.DockingInstructionSet().mem(mem_instruction, starting_world)

        self.assertEqual(new_world['memory'][8], 73)

class PartOneComputerTest(unittest.TestCase):

    def test_address_sum_example(self):
        print('test exmaple')
        instructions = fourteen.main.parse("fourteen/example.txt")
        dc = fourteen.main.PartOneComputer()
        dc.run(instructions)
        self.assertEqual(fourteen.main.address_sum(dc), 165) 

    def test_address_sum_puzzle(self):
        print('test puzzle')
        dc = fourteen.main.PartOneComputer()
        instructions = fourteen.main.parse("fourteen/puzzle.txt")
        dc.run(instructions)
        self.assertEqual(fourteen.main.address_sum(dc), 11884151942312)

