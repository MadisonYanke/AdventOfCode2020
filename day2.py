def getValidPasswords(filename):
    validPasswords = 0
    with open(filename) as inFile:
        for line in inFile:
            minchar = int(line[0 : line.find('-')])
            maxchar = int(line[line.find('-') + 1 : line.find(' ')])
            char = line[line.find(' ') + 1: line.find(':')]
            charnumber = line[line.find(':') + 1 :].count(char)
            if minchar <= charnumber <= maxchar:
                validPasswords += 1
    return validPasswords

def getValidPasswords2(filename):
    validPasswords = 0
    with open(filename) as inFile:
        for line in inFile:
            pos1 = int(line[0 : line.find('-')])
            pos2 = int(line[line.find('-') + 1 : line.find(' ')])
            char = line[line.find(' ') + 1: line.find(':')]
            password = line[line.find(':') + 2:]
            if (password[pos1-1] == char) ^ (password[pos2-1] == char):
                validPasswords += 1
    return validPasswords

print getValidPasswords('day2input.txt')
print getValidPasswords2('day2input.txt')