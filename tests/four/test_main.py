import unittest
import four.main

class PassportTest(unittest.TestCase):
    def test_passport(self):
        self.assertEqual(len(four.main.read_passports("four/data_example.txt")),4) 

    def test_passport_create(self):
        lines = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
                 'byr:1937 iyr:2017 cid:147 hgt:183cm']

        p = four.main.Passport(lines)
        self.assertIsInstance(p, four.main.Passport)

    def test_passport_fields(self):
        lines = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
                 'byr:1937 iyr:2017 cid:147 hgt:183cm']

        p = four.main.Passport(lines)
        self.assertEqual(len(p.fields), 8)

    def test_passport_is_valid(self):
        lines = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
                 'byr:1937 iyr:2017 cid:147 hgt:183cm']

        p = four.main.Passport(lines)
        self.assertTrue(p.is_valid())

    def test_passport_is_not_valid(self):
        lines = ['iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
                 'hcl:#cfa07d byr:1929',]

        p = four.main.Passport(lines)
        self.assertFalse(p.is_valid())

    def test_num_of_example_valid_passports(self):
        passports = four.main.read_passports("four/data_example.txt")
        self.assertEqual(len(list(filter(lambda p: p.is_valid(), passports))), 2)

    def test_num_of_example_valid_passports_puzzle(self):
        passports = four.main.read_passports("four/data_puzzle.txt")
        self.assertEqual(len(list(filter(lambda p: p.is_valid(), passports))), 160)

    def test_get_field(self):
        lines = ['iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
                 'hcl:#cfa07d byr:1929',]

        p = four.main.Passport(lines)
        field = p.get_field('iyr')
        self.assertEqual(field.name, 'iyr')
        self.assertEqual(field.value, '2013')

    def test_bry_is_valid(self):
        self.assertTrue(four.main.Passport(['byr:2002']).is_field_valid('byr'))

    def test_bry_is_valid(self):
        self.assertFalse(four.main.Passport(['byr:2003']).is_field_valid('byr'))

    def test_iyr_is_valid(self):
        self.assertTrue(four.main.Passport(['iyr:2010']).is_field_valid('iyr'))

    def test_iyr_is_not_valid(self):
        self.assertFalse(four.main.Passport(['iyr:2009']).is_field_valid('iyr'))

    def test_eyr_is_valid(self):
        self.assertTrue(four.main.Passport(['eyr:2030']).is_field_valid('eyr'))

    def test_eyr_is_not_valid(self):
        self.assertFalse(four.main.Passport(['eyr:2031']).is_field_valid('eyr'))

    def test_hcl_is_valid(self):
        self.assertTrue(four.main.Passport(['hcl:#123abc']).is_field_valid('hcl'))

    def test_hcl_is_not_valid(self):
        self.assertFalse(four.main.Passport(['hcl:#123abz']).is_field_valid('hcl'))

    def test_hcl_is_not_valid2(self):
        self.assertFalse(four.main.Passport(['hcl:123abc']).is_field_valid('hcl'))

    def test_ecl_is_valid(self):
        self.assertTrue(four.main.Passport(['ecl:brn']).is_field_valid('ecl'))

    def test_ecl_is_valid2(self):
        self.assertTrue(four.main.Passport(['ecl:hzl']).is_field_valid('ecl'))

    def test_ecl_is_not_valid(self):
        self.assertFalse(four.main.Passport(['ecl:wat']).is_field_valid('ecl'))

    def test_pid_is_valid(self):
        self.assertTrue(four.main.Passport(['pid:000000001']).is_field_valid('pid'))

    def test_pid_is_not_valid(self):
        self.assertFalse(four.main.Passport(['pid:0123456789']).is_field_valid('pid'))

    def test_hgt_is_valid(self):
        self.assertTrue(four.main.Passport(['hgt:60in']).is_field_valid('hgt'))

    def test_hgt_is_valid(self):
        self.assertTrue(four.main.Passport(['hgt:190cm']).is_field_valid('hgt'))

    def test_hgt_is_not_valid(self):
        self.assertFalse(four.main.Passport(['hgt:190in']).is_field_valid('hgt'))

    def test_hgt_is_not_valid(self):
        self.assertFalse(four.main.Passport(['hgt:190']).is_field_valid('hgt'))

    def test_valid_passports(self):
        passports = four.main.read_passports("four/data_valid.txt")

        self.assertEqual(len(list(filter(lambda p: p.is_valid(), passports))), 4)

    def test_invalid_passports(self):
        passports = four.main.read_passports("four/data_invalid.txt")

        self.assertEqual(len(list(filter(lambda p: not p.is_valid(), passports))), 4)

    def test_get_validations_for(self):
        lines = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
                 'byr:1937 iyr:2017 cid:147 hgt:183cm']

        p = four.main.Passport(lines)
        validations = list(p.validations_for('byr'))
        k, v = next(p.validations_for('byr'))

        self.assertEqual(len(validations), 2)
        self.assertTrue(callable(v))


