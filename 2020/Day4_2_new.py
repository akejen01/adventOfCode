# Day4_1
# coding=utf-8



def checkBry(value):
    return  1920 <= int(value) <= 2002

def checkIyr(value):
    return 2010 <= int(value) <= 2020

def checkEyr(value):
    return 2020 <= int(value) <= 2030

def checkHgt(value):
    # kolla så att det är ett 
    if ('in' in value):
        return int(value[:-2]) in range(59, 77)
    if ('cm' in value):
        return int(value[:-2]) in range(150, 194)
    return False

def checkHcl(value):
    return value[0] == '#' and len(value) == 7 and value[1:].isalnum()

def checkEcl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def checkPid(value):
    return len(value) == 9 and value.isnumeric()

def checkAttribute(attribute):
    key = attribute.split(':')[0]
    value = attribute.split(':')[1]
    returnValue = False

    if (key == 'byr'):
        returnValue = checkBry(value)
    if (key == 'iyr'):
        returnValue = checkIyr(value)
    if (key == 'eyr'):
        returnValue = checkEyr(value)
    if (key == 'hgt'):
        returnValue = checkHgt(value)
    if (key == 'hcl'):
        returnValue = checkHcl(value)
    if (key == 'ecl'):
        returnValue = checkEcl(value)
    if (key == 'pid'):
        returnValue = checkPid(value)
    return returnValue

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isPassportValid(passport):
    for field in fields:
        if field not in passport:
            return False
    return True


with open('Day4_1_input.txt') as f:
    data = f.readlines()
    data = [ line.strip() for line in data]
    
validCount = 0
validPassports = []
currentPassport = ''

for line in data:
    if line != '':
        currentPassport += ' ' + line

    else:
        if isPassportValid(currentPassport):
            validCount += 1
            validPassports.append(currentPassport)
        
        currentPassport = ''

if isPassportValid(currentPassport):
    validCount += 1

print(validPassports)
print(validCount)