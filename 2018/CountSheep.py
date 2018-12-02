# FoldAnArray.py
# coding=utf-8


"""
8 kyu

Wilson primes satisfy the following condition. Let P represent a prime number.

Then ((P-1)! + 1) / (P * P) should give a whole number.

Your task is to create a function that returns true if the given number is a Wilson prime.

"""
from __future__ import division
import unittest, math


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(wilsonPrime(13), True)

    def test_2(self):
        self.assertEqual(wilsonPrime(5), True)

    def test_3(self):
        self.assertEqual(wilsonPrime(7), False)

    def test_4(self):
        self.assertEqual(wilsonPrime(0), False)

    def test_5(self):
        self.assertEqual(wilsonPrime(1), False)


def primeNumber(num):
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                #print(num,"is not a prime number")
                #print(i,"times",num//i,"is",num)
                break
        else:
            #print(num,"is a prime number")
            if (wilsonPrime(num)):
                print(num," is also a wilson prime!")

       
    # if input number is less than
    # or equal to 1, it is not prime
    #else:
        #print(num,"is not a prime number")




def count_sheep(n):
    returnString= ""
    for i in range(1,n +1):
        returnString.join(str(i) + " sheep...")
    return returnString


def main():
    print(count_sheep(3))


if __name__ == "__main__":
    #unittest.main()
    main()