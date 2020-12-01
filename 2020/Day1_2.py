# Day1_2
# coding=utf-8


"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""
import unittest, math


class TestMethod(unittest.TestCase):

     def test_1(self):
         self.assertEqual(checkIf2020(2010, 10), True)

     def test_2(self):
         self.assertEqual(checkIf2020(2000, 10), False)



def checkIf2020(a, b, c):
    if (a + b + c == 2020):
        return True
    else:
        return False


def main():
    with open('Day1_1_input.txt') as f:
        lines = f.read().splitlines()

    for a in lines:
        for b in lines:
            for c in lines:
                if (checkIf2020(int(a), int(b), int(c))):
                    print("Häpp! " + str(int(a) * int(b) * int(c)))
                




    #print("Double: " + str(findFrequenceDouble(lines)))

    

if __name__ == "__main__":
    #unittest.main()
    main()