import re

def CheckPassports(validFields, passportList, rules = None, validate=False):
    validPassports = 0
    for passport in passportList:
        passportFields = [i[0] for i in passport]
        validPassport = set(validFields).issubset(passportFields)
        if validate and validPassport: validPassport = ValidatePassport(passport, rules)
        if validPassport:
            validPassports += 1
    return validPassports

def ValidatePassport(passport, rules):
    for field in passport:
        try:
            if re.match(rules[field[0]], field[1]) is None: return False
        except KeyError:
            continue
    return True

passports = []
with open('day4input.txt') as f:
    lines = f.read().split('\n\n')
    for line in lines:
        passports.append([fields.split(':') for fields in line.split()])

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
rules = {'byr': r'^(19[2-9][0-9]|200[0-2])$',
         'iyr': r'^(201[0-9]|2020)$',
         'eyr': r'^(202[0-9]|2030)$',
         'hgt': r'^((1[5-8][0-9]cm|19[0-3]cm)|(59in|6[0-9]in|7[0-6]in))$',
         'hcl': r'^#[0-9a-f]{6}$',
         'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
         'pid': r'^\d{9}$'}


print(CheckPassports(requiredFields, passports))
print(CheckPassports(requiredFields, passports, rules, True))


