# Day1_2
# coding=utf-8


"""


"""
import unittest, math


class TestMethod(unittest.TestCase):


     def test_1(self):
        self.assertEqual(intCodeComputer(['1','0','0','0','99']),['2','0','0','0','99'] )

     def test_2(self):
        self.assertEqual(intCodeComputer(['2','3','0','3','99']),['2','3','0','6','99'] )

     def test_3(self):
        self.assertEqual(intCodeComputer(['2','4','4','5','99','0']),['2','4','4','5','99','9801'] )

     def test_4(self):
        self.assertEqual(intCodeComputer(['1','1','1','4','99','5','6','0','99']),['30','1','1','4','2','5','6','0','99'] )



def main():
    print("Start!")
    with open('Day2_1_data.txt') as f:
        lines = f.read().splitlines()

    for l in lines:
        charArray = l.split(',')


    finalArray=intCodeComputer(charArray)
    print("Done!: " + str(finalArray))


def intCodeComputer(commandArray):
    for i in range(0,len(commandArray), 4):
        optCode = int(commandArray[i])
        
        if (optCode == 1):
            posValueA = int(commandArray[i+1])
            posValueB = int(commandArray[i+2])
            storeValue = int(commandArray[posValueA]) + int(commandArray[posValueB])
            posStore = int(commandArray[i+3])
            commandArray[posStore] = str(storeValue)
        if (optCode == 2):
            posValueA = int(commandArray[i+1])
            posValueB = int(commandArray[i+2])
            storeValue = int(commandArray[posValueA]) * int(commandArray[posValueB])
            posStore = int(commandArray[i+3])
            commandArray[posStore] = str(storeValue)

    return commandArray


    

    

if __name__ == "__main__":
    #unittest.main()
    main()