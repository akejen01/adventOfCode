# Day1_1
# coding=utf-8


"""
After feeling like you've been falling for a few minutes, you look at the device's tiny screen. "Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock." Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

    Current frequency  0, change of +1; resulting frequency  1.
    Current frequency  1, change of -2; resulting frequency -1.
    Current frequency -1, change of +3; resulting frequency  2.
    Current frequency  2, change of +1; resulting frequency  3.

In this example, the resulting frequency is 3.

Here are other example situations:

    +1, +1, +1 results in  3
    +1, +1, -2 results in  0
    -1, -2, -3 results in -6

Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

--- Part Two ---

You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

    Current frequency  0, change of +1; resulting frequency  1.
    Current frequency  1, change of -2; resulting frequency -1.
    Current frequency -1, change of +3; resulting frequency  2.
    Current frequency  2, change of +1; resulting frequency  3.
    (At this point, the device continues from the start of the list.)
    Current frequency  3, change of +1; resulting frequency  4.
    Current frequency  4, change of -2; resulting frequency  2, which has already been seen.

In this example, the first frequency reached twice is 2. Note that your device might need to repeat its list of frequency changes many times before a duplicate frequency is found, and that duplicates might be found while in the middle of processing the list.

Here are other examples:

    +1, -1 first reaches 0 twice.
    +3, +3, +4, -2, -4 first reaches 10 twice.
    -6, +3, +8, +5, -6 first reaches 5 twice.
    +7, +7, -2, -7, -4 first reaches 14 twice.

What is the first frequency your device reaches twice?

"""
import unittest


class TestMethod(unittest.TestCase):

    # def test_1(self):
    #     self.assertEqual(frequencyChangeSum([+1, +1, +1]), 3)

    # def test_2(self):
    #     self.assertEqual(frequencyChangeSum([+1, +1, -2]), 0)

    # def test_3(self):
    #     self.assertEqual(frequencyChangeSum([-1, -2, -3]), -6)

    # def test_4(self):
    #     self.assertEqual(frequencyChangeSum(['+15', '-7', '+16', '+5']), 29)

    def test_5(self):
        self.assertEqual(findFrequenceDouble([+1,-2,+3,+1,+1,-2]),2)

    def test_6(self):
        self.assertEqual(findFrequenceDouble(['+3', '+3', '+4', '-2','-4']), 10)

    def test_7(self):
        self.assertEqual(findFrequenceDouble([-6, +3, +8, +5, -6]), 5)

    def test_8(self):
        self.assertEqual(findFrequenceDouble([+7, +7, -2, -7, -4]), 14)


def frequencyChangeSum(numbers):
    return sum(map(lambda x : int(x), numbers))





def findFrequenceDouble(numbers):
    currentFrequence = 0 # Always start on 0
    foundFrequences =[]
    found = False
    doubleFrequence = 0  
    times = 0

    while( found == False ):
        times = times + 1
        print("Current loop: " + str(times))
        for frequence in numbers:
            currentFrequence = currentFrequence + int(frequence)

            for i in range(len(foundFrequences)):
                if (currentFrequence == foundFrequences[i] and found == False):
                    found = True
                    doubleFrequence = currentFrequence
                    break
            foundFrequences.append(currentFrequence)

    return doubleFrequence    

                


def main():
    with open('Day1_1_data.txt') as f:
        lines = f.read().splitlines()
    #print(lines)

    print("Sum: " + str(frequencyChangeSum(lines)))
    print("Double: " + str(findFrequenceDouble(lines)))

    

if __name__ == "__main__":
    #unittest.main()
    main()