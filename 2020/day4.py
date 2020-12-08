# Day4_1
# coding=utf-8

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isPassportValid(passport):
    for field in fields:
        if field not in passport:
            return False
    print(passport)
    return True


with open('Day4_1_input.txt') as f:
    data = f.readlines()
    data = [ line.strip() for line in data]
    
validCount = 0

currentPassport = ''
for line in data:
    if line != '':
        currentPassport += ' ' + line

    else:
        if isPassportValid(currentPassport):
            validCount += 1

        currentPassport = ''

if isPassportValid(currentPassport):
    validCount += 1

print(validCount)