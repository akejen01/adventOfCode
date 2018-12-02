# BitCounting
# coding=utf-8


"""
6 kyu

Bit Counting

Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


"""
import unittest


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(bitCounting(8), 1)

    def test_2(self):
        self.assertEqual(bitCounting(33), 2)

    def test_3(self):
        self.assertEqual(bitCounting(357), 5)

    def test_4(self):
        self.assertEqual(bitCounting(-21), 3)




def bitCounting(number):
    return len('{0:b}'.format(abs(number)).replace("0",""))


def main():
    print("Text")
    

if __name__ == "__main__":
    unittest.main()
    #main()