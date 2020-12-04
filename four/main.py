import collections
import re

Field = collections.namedtuple('Field', ['name', 'value'])
def read_passports(filename):
    passports = []
    with open(filename) as f:
        lines = f.readlines()

    passport_lines = []
    for line in lines:
        if line.strip() == "":
            passports.append(Passport(passport_lines))
            passport_lines.clear()
        else:
            passport_lines.append(line)
    if len(passport_lines) > 0:
        passports.append(Passport(passport_lines))

    return passports
def height_validation(f):
    result = re.search("(?P<num>[0-9]+)(?P<units>in|cm)", f)

    if result is None:
        return False

    elif result.group('units') == 'in':
        return 59 <= int(result.group('num')) <=76
    elif result.group('units') == 'cm':
        return 150 <= int(result.group('num')) <= 193

    return False




class Passport():
    valid_fields = sorted(['byr','iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    validations = (
        ('byr',lambda f: bool(re.search("^[0-9]{4}$", f))),
        ('byr',lambda f: 1920 <= int(f) <= 2002),

        ('iyr',lambda f: bool(re.search("^[0-9]{4}$", f))),
        ('iyr',lambda f: 2010 <= int(f) <= 2020),

        ('eyr',lambda f: bool(re.search("^[0-9]{4}$", f))),
        ('eyr',lambda f: 2020 <= int(f) <= 2030),

        ('hgt', height_validation),

        ('hcl',lambda f: bool(re.search("^#[0-9a-f]{6}$", f))), 

        ('ecl',lambda f: f in ['amb', 'blu', 'brn', 'gry', 'grn','hzl', 'oth']) ,

        ('pid', lambda f: bool(re.search("^[0-9]{9}$", f))),


    )

    def __init__(self, lines):
        self.fields = []
        for line in lines:
            for item in line.split(" "):
                k, v = item.split(":")
                self.fields.append(Field(k,v.strip()))

    def is_valid(self):
        passport_fields = [ field.name for field in self.fields ]
        return all(valid_field in passport_fields and self.is_field_valid(valid_field) for valid_field in self.valid_fields)

    def get_field(self, code):
        return next(filter(lambda f: f.name == code, self.fields), None)

    def validations_for(self, code):
        return filter(lambda i: i[0] == code, self.validations)

    def is_field_valid(self, code):
        f = self.get_field(code)
        return all(v(f.value) for k, v in self.validations_for(f.name))
