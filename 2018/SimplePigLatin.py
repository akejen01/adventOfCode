# Simple Pig Latin

import unittest


"""
5 kyu

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !


"""


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")

    def test_2(self):
        self.assertEqual(pig_it("Hello world !"), "elloHay orldway !")



def pig_it(string):

    stringArray = string.split()
    returnString = ""
    firstWord = True

    for S in stringArray:
    
        if ( firstWord == False ):
            returnString = returnString + " "
        firstWord = False
        
        for c in S:
            if ( c.isalnum() == False):
            



        returnString = returnString + S[1:]+S[0]+"ay" 

    return returnString
    
      
    

def main():
    S="Hello world !"
    #print(S[1:]+S[0]+"ay")
    print(pig_it("Pig latin is cool"))
    print(pig_it("Hello world !"))
    
    print "".join([ c if c.isalnum() else "*" for c in S ])





if __name__ == "__main__":
    #unittest.main()
    main()