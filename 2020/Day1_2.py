# Day1_2
# coding=utf-8


"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

itertools

"""
import unittest, math, itertools, operator


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(checkIf2020(2010, 10, 0), True)

    def test_2(self):
        self.assertEqual(checkIf2020(2000, 10, 5), False)

    def test_3(self):
        self.assertEqual(calculateValueItertools([1721,979,366,299,675,1456]), 241861950)



def checkIf2020(a, b, c):
    if (int(a) + int(b) + int(c) == 2020):
        return True
    else:
        return False


def calculateValue(lines):
    for a in lines:
        for b in lines:
            for c in lines:
                if (checkIf2020(int(a), int(b), int(c))):
                    return (int(a) * int(b) * int(c))

def calculateValueItertools(lines):
    for a, b, c in list(itertools.combinations(lines, 3)):
        if (a + b + c == 2020):
            return a * b * c

def calculateValueItertoolsOneMore(lines):
    for c in itertools.combinations(lines, 3):
        if (list(itertools.accumulate(c))[-1] == 2020):
            return list(itertools.accumulate(c, operator.mul))[-1]


def main():

#   Alternativt kan man läsa in med:
    with open('Day1_1_input.txt') as f:
        entries = [int(e) for e in set(f.read().splitlines())]
    f.close()
    
    print("Calc 1: " + str(calculateValue(entries))) 
    
    print("Calc 2: " + str(calculateValueItertools(entries))) 

    print("Calc 3: " + str(calculateValueItertoolsOneMore(entries)))

    

if __name__ == "__main__":
    #unittest.main()
    main()