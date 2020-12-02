# Day2_1
# coding=utf-8


"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?


"""
import unittest, math, itertools, operator


class TestMethod(unittest.TestCase):

    def test_1(self):
         self.assertEqual(countsOfCharInPassword('aasffbgd', 'd'), 1)

    def test_2(self):
         self.assertEqual(countsOfCharInPassword('aasffbgd', 't'), 0)

    def test_3(self):
         self.assertEqual(countsOfCharInPassword('aasffbgd', 'ö'), 0)

    def test_4(self):
         self.assertEqual(countsOfCharInPassword('aasffbgd', 'a'), 2)

    def test_5(self):
        self.assertEqual(isCharCountInRange(2, 5, 2), True)

    def test_6(self):
        self.assertEqual(isCharCountInRange(2, 5, 1), False)



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
        lowerRange = int(instruction[0])
        upperRange = int(instruction[1])
        char = l.split(':')[0].split(' ')[1]
        password = l.split(':')[1]
        if (countsOfCharInPassword(password, char) > 0):
            if(isCharCountInRange(lowerRange, upperRange, countsOfCharInPassword(password, char))):
                print(l)
                counts = counts + 1
    print("Antal : " + str(counts))



    

if __name__ == "__main__":
    #unittest.main()
    main()