# SquareSum
# coding=utf-8


"""
8 kyu

Complete the square sum method so that it squares each number passed into it and then sums the results together.

For example: 
squareSum([1, 2, 2]) should return 9 because 1^2 + 2^2 + 2^2 = 9.
squareSum([2,5,6,3]) should return 74 because 2^2 + 5^2 + 6^2 + 3^2 = 74
squareSum([0]) should return 0 because 0^2 = 0


"""
import unittest


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(squareSum([1, 2, 2]), 9)


def squareSum(numbers):
    return sum(map(lambda x : pow(x,2), numbers))


def main():
    print(squareSum([0]))
    

if __name__ == "__main__":
    #unittest.main()
    main()