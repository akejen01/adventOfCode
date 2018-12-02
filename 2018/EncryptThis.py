# Encrypt This

import unittest


"""
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
        The first letter needs to be converted to its ASCII code.
        The second letter needs to be switched with the last letter
    Keepin' it simple: There are no special characters in input.

Examples:

encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"

"""


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(encrypt_this("Hello"), "72olle")

    def test_2(self):
        self.assertEqual(encrypt_this("good"), "103doo")

    def test_3(self):
        self.assertEqual(encrypt_this("hello world"), "104olle 119drlo")        



def encrypt_this(string):

    stringArray = string.split()
    returnString = ""

    for word in stringArray:

        for index in range(len(word)):

            if( index == 0):
                returnString = returnString + (str(ord(word[index])))
            elif( index == 1):
                returnString = returnString + word[len(word) -1]
            elif( index == len(word) -1 ):
                returnString = returnString + (word[1])        
            else:
                returnString = returnString + (word[index])

        if (len(stringArray) > 1 ):
            returnString = returnString + " "

    if(len(stringArray) > 1):
        return returnString[:-1]
    else:
        return returnString
    
      
    

def main():
    print("Tjoho: " + encrypt_this("Hello"))
    

if __name__ == "__main__":
    unittest.main()
    #main()