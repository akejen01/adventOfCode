# BitCounting
# coding=utf-8


"""
8 kyu

Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

"""
import unittest


class TestMethod(unittest.TestCase):

    def test_1(self):
        self.assertEqual(lovefunc(1,4), True)

    def test_2(self):
        self.assertEqual(lovefunc(2,2), False)

    def test_3(self):
        self.assertEqual(lovefunc(0,1), True)

    def test_4(self):
        self.assertEqual(lovefunc(0,0), False)

    def test_5(self):
        self.assertEqual(lovefunc(639, 945), False)




# def lovefunc(flower1, flower2):
#     petals1 = flower1 % 2 == 0
    
#     petals2 = flower2 % 2 == 0

#     if ((petals1 == petals2) ):
#         return False
#     else:
#         return True


lovefunc=lambda a,b:(a+b)%2
  



def main():
    print("Text")
    
    

if __name__ == "__main__":
    unittest.main()
    #main()