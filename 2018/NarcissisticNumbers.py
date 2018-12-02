# NarcissisticNumbers.py
# coding=utf-8

'''
6 kyu



'''

import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_narcissistic(10), False)

    def test_2(self):
        self.assertEqual(is_narcissistic(153), True)


def is_narcissistic(i):
    tal = 0
    length = len(str(i))

    for n in str(i):
        deltal = pow(int(n),length)
        tal = tal + deltal

    if (tal == i ):
        return True
    else:
        return False



def main():
    print("Run the tests!")



if __name__ == "__main__":
    unittest.main()
    #main()

