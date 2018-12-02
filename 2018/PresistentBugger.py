# PresistentBugger
# coding=utf-8

#import functools
from random import randint

"""
6 kyu

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.



"""
import unittest


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(persistence(39), 3)

    def test_2(self):
        self.assertEqual(persistence(999), 4)

    def test_3(self):
        self.assertEqual(persistence(4), 0)

    def test_4(self):
        self.assertEquals(persistence(25), 2)        




#-----------------
def soluce(n):
        digits = [int(d) for d in str(n)]
        if (len(digits) == 1):
            return 0
        p = reduce(lambda x, y : x * y, digits, 1)
        return 1 + persistence(p)
#-----------------

Test.it("Basic tests")
Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)
Test.assert_equals(persistence(444), 3)

Test.describe("Random tests")
for _ in xrange(50):
    n = randint(1, 500000)
    Test.it("Testing for: " + str(n))  
    Test.assert_equals(persistence(n), soluce(n))



def persistence(number):

    returnValue = 0

    numberArray = map(int, str(number)); 
    cont = True
    multiplyValue = 0

    if (len(numberArray) == 1 ) :
        return 0
    else:
        while(cont == True):
            print("in loop")
            multiplyValue = 1
            for currentValue in numberArray:
                multiplyValue = multiplyValue * currentValue
                print(" multiplyValue: %s  currentValue: %s" % (multiplyValue , currentValue))
                if (multiplyValue == 0):
                    return returnValue
                else:
                    returnValue += 1
                    if(len(str(multiplyValue)) == 1 ):
                        cont = False
                    
        
        return returnValue

def main():
    print("ReturnValue: " +str(persistence(25)))
    

if __name__ == "__main__":
    #unittest.main()
    main()