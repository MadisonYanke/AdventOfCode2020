import re

def CheckPassports(validFields, passportList, validate=False):
    validPassports = 0
    for passport in passportList:
        validPassport = True
        for field in validFields:
                if field not in (i[0] for i in passport):
                    validPassport = False
        if validate and validPassport:
            validPassport = ValidatePassport(passport)
        if validPassport:
            validPassports += 1
            print(passport)
    return validPassports

def ValidatePassport(passport):
    for field in passport:
        if field[0].strip() == 'byr' and ((1920 <= int(field[1]) <= 2002) == False): return False
        elif field[0].strip() == 'iyr' and ((2010 <= int(field[1]) <= 2020) == False): return False
        elif field[0].strip() == 'eyr' and ((2020 <= int(field[1]) <= 2030) == False):return False
        elif field[0].strip() == 'hgt' and ((re.match(r'(^1[5-8][0-9]cm$|^19[0-3]cm$)|(^59in$|^6[0-9]in$|^7[0-6]in$)', field[1])) == None): return False
        elif field[0].strip() == 'hcl' and ((re.match(r'^#[0-9a-f]{6}$', field[1])) == None): return False
        elif field[0].strip() == 'ecl' and ((field[1] in ['amb','blu','brn','gry','grn','hzl','oth']) == False): return False
        elif field[0].strip() == 'pid' and ((re.match(r'^\d{9}$', field[1])) == None): return False
    return True

passports = []
with open('day4input.txt') as f:
    lines = f.read().split('\n\n')
    for line in lines:
        passports.append([fields.split(':') for fields in line.split()])

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
print(CheckPassports(fields, passports))
print(CheckPassports(fields, passports, True))


