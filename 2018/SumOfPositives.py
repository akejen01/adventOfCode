# Sum of potitives
# coding=utf-8


"""
8 kyu

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.



"""
import unittest


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sumOfPositives([1, 2, 2]), 5)

    def test_2(self):
        self.assertEqual(sumOfPositives([1,-4,7,12]), 20)

    def test_3(self):
        self.assertEqual(sumOfPositives([-1,-4,-7,-12]), 0)




def sumOfPositives(numbers):
    #sum(map(lambda x :  x if x > 0 else 0 , numbers))
    totalSum = 0
    for x in numbers:
        if (x > 0):
            totalSum = totalSum + x
    return totalSum


def main():
    print(sumOfPositives([0]))
    

if __name__ == "__main__":
    unittest.main()
    #main()