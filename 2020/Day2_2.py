# Day2_2
# coding=utf-8


"""
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

"""
import unittest, math, itertools, operator


class TestMethod(unittest.TestCase):

    def test_7(self):
        self.assertEqual(isCharPosCorrect(1, 3, 'a', 'abcde'), True)

    def test_8(self):
        self.assertEqual(isCharPosCorrect(1, 3, 'b', 'cdefg'), False)

    def test_9(self):
        self.assertEqual(isCharPosCorrect(2, 9, 'c', 'ccccccccc'), False)

    def test_10(self):
        self.assertEqual(isCharPosCorrect(1, 3, 'e', 'cdefg'), True)

    def test_11(self):
        self.assertEqual(isCharPosCorrect(1, 3, 'e', 'egefg'), False)

    def test_12(self):
        self.assertEqual(isCharPosCorrect(1, 2, 'w', 'wwwwt'), False)

    def test_13(self):
        self.assertEqual(isCharPosCorrect(5, 7, 'h', 'hrhdnhmhhhnx'), False)

    def test_14(self):
        self.assertEqual(isCharPosCorrect(12, 13, 'n', 'nwnwdplnhfhlnnnntfn'), True)



def isCharPosCorrect(firstPos, secondPos, char, password):
    returnValue = False
    if (password[firstPos-1] == char and password[secondPos-1] != char):
        returnValue = True
    if (password[secondPos-1] == char and password[firstPos-1] != char):
        returnValue = True
    return returnValue

def isCharCountInRange(lowerRange, upperRange, count):
    return count >= lowerRange and count <= upperRange


def countsOfCharInPassword(password, char):
    return password.count(char)


def main():
    with open('Day2_1_input.txt') as f:
        lines = f.read().splitlines()
    f.close()

    counts = 0
    for l in lines:
        instruction = l.split(':')[0].split(' ')[0].split('-') 
        firstPos = int(instruction[0])
        secondPos = int(instruction[1])
        char = l.split(':')[0].split(' ')[1]
        password = l.split(':')[1].strip()
        if(isCharPosCorrect(firstPos, secondPos, char, password)):
            counts = counts + 1
    print("Antal : " + str(counts))

if __name__ == "__main__":
    #unittest.main()
    main()


