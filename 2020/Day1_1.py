# Day1_1
# coding=utf-8


"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


"""
import unittest, math, itertools, operator


class TestMethod(unittest.TestCase):

    def test_1(self):
         self.assertEqual(checkIf2020(2010, 10), True)

    def test_2(self):
         self.assertEqual(checkIf2020(2000, 10), False)

    def test_3(self):
        self.assertEqual(calculateValueItertools([1721,979,366,299,675,1456]), 514579)



def checkIf2020(a, b):
    if (a + b == 2020):
        return True
    else:
        return False


def calculateValue(lines):
    for l in lines:
        for n in lines:
            if (checkIf2020(int(l), int(n))):
                return (int(l) * int(n))

def calculateValueItertools(lines):
    for a, b in itertools.combinations(lines, 2):
        if (a + b == 2020):
            return a * b

def main():
    with open('Day1_1_input.txt') as f:
        entries = [int(e) for e in set(f.read().splitlines())]
    f.close()
  
    print("Värde: " + str(calculateValueItertools(entries)))

if __name__ == "__main__":
    unittest.main()
    #main()