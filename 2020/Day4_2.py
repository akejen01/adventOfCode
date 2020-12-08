# Day4_2
# coding=utf-8

"""

"""
import unittest, math, itertools, operator


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(checkBry('2002'), True)

    def test_2(self):
        self.assertEqual(checkBry('1919'), False)
        
    def test_3(self):
        self.assertEqual(checkAttribute('bry:2003'), False)

    def test_4(self):
        self.assertEqual(checkAttribute('bry:1920'), True)

    def test_5(self):
        self.assertEqual(checkAttribute('iyr:2011'), True)

    def test_6(self):
        self.assertEqual(checkAttribute('iyr:2009'), False)

    def test_7(self):
        self.assertEqual(checkAttribute('eyr:2030'), True)
    
    def test_8(self):
        self.assertEqual(checkAttribute('hgt:59in'), True)

    def test_9(self):
        self.assertEqual(checkAttribute('hcl:#123abc'), True)

    def test_10(self):
        self.assertEqual(checkAttribute('hcl:dab227'), False)

    def test_11(self):
        self.assertEqual(checkAttribute('ecl:blu'), True)

    def test_12(self):
        self.assertEqual(checkAttribute('pid:080248884'), True)

    def test_13(self):
        self.assertEqual(checkAttribute('pid:000000000'), True)

    def test_14(self):
        self.assertEqual(checkAttribute('cid:000000000'), True)




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
    if (key == 'cid'):
        returnValue = True

    return returnValue



def checkPassport(passport):
    valid = False
    for attribute in passport:
        valid = checkAttribute(attribute)
    return valid


def main():
    f = open('Day4_1_input_example.txt', 'r') 
    count = 0
    validPassports = 0
    passports = []
    passport = []
    while True:
        line = f.readline()
        #print(line)
        elements = line.strip().split(' ')
        for e in elements:
            if (e != ''):
                if (e.split(':')[0] != 'cid'):
                    passport.append(e)

        if(line == '\n'):
            passports.append(passport)
            #print(passport)
            passport = []

        if not line: 
            break
    
    for p in passports:

        if (len(p) == 7):
            #print("Pre valid:  "+ str(p))
            if (checkPassport(p)):
                #print("Post valid: " + str(p))
                validPassports += 1
            else:
                print("Invalid   : " + str(p))
        

    print("Antal gällande pass: {}".format(validPassports))


if __name__ == "__main__":
    #unittest.main()
    main()