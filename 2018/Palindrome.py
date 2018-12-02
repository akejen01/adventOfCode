# DNA_to_RNA_Conversion.py
'''
6 kyu
A friend of mine told me privately: "I don't like palindromes". "why not?" - I replied. "Because when I want to do some programming challenges, I encounter 2 or 3 ones first related with palindromes. I'm fed up" - he confess me with anger. I said to myself:"Thankfully, that doesn't happen in Codewars". Talking seriously, we have to count the palindrome integers. Doing that, perhaps, it will help us to make all the flood of palindrome programming challenges more understandable.

For example all the integers of 1 digit (not including 0) are palindromes, 9 cases. We have nine of them with two digits, so the total amount of palidromes below 100 (102) is 18. At least, will we be able to calculate the amount of them for a certain number of digits? Let's say for 2000 digits? Prepare a code that given the number of digits n, may output the amount of palindromes of length equals to n and the total amount of palindromes below 10n.

You will see more examples in the box. Happy coding!!

(You don't know what palindromes are? Investigate, :))

'''

import unittest


class TestPalindromeForNumber(unittest.TestCase):

    def test_palindromeTo100(self):
        self.assertEqual(palidromeOfNumbers(100), 18)

    def test_DNAtoRNAWithT(self):
        self.assertEqual(palidromeOfNumbers(2000), 118)




def palidromeOfNumbers(number):
    numberOfPalindromes = 0

    palindromeNumbers = range(1, number + 1)

    for number in palindromeNumbers:
        currentNumberAsString = str(number)
        if ( currentNumberAsString == currentNumberAsString[::-1]):
            numberOfPalindromes += 1


    return numberOfPalindromes






def main():
    print("Palindrom : ")
    print ("100 : " + str(palidromeOfNumbers(100)))
    print ("200 : " + str(palidromeOfNumbers(200)))



if __name__ == "__main__":
    #unittest.main()
    main()

