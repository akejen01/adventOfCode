# OnesAndZeros
# coding=utf-8


"""
7 kyu
Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

However, the arrays can have varying lengths, not just limited to 4.

"""
import unittest


class TestBinaryToIntegerMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(onesAndZeros([0,0,0,1]), 1)

    def test_2(self):
        self.assertEqual(onesAndZeros([0,0,1,1]), 3)

    def test_3(self):
        self.assertEqual(onesAndZeros([0,1,1,1]), 7)

    def test_4(self):
        self.assertEqual(onesAndZeros([1,0,0,1]), 9)

    def test_5(self):
        self.assertEqual(onesAndZeros([0,0,0,0]), 0)

    def test_5(self):
        self.assertEqual(onesAndZeros([1,0,1,1,0,0,1,0,1]), 357)


def onesAndZeros(bitArray):

    indexValue = 0
    integerValue = 0

    for bitValue in reversed(bitArray):

        integerValue =  integerValue + (bitValue * pow(2,indexValue))
        indexValue += 1

    return integerValue

def main():
    print("Text")
    

if __name__ == "__main__":
    unittest.main()
    #main()