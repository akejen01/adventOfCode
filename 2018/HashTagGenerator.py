# HashTagGenerator
"""
5 kyu
The marketing team are spending way too much time typing in hashtags.

Let's help them with out own Hashtag Generator!

Here's the deal:

    If the final result is longer than 140 chars it must return false.
    If the input is a empty string it must return false.
    It must start with a hashtag (#).
    All words must have their first letter capitalized.

Example Input to Output:

" Hello there thanks for trying my Kata" => "#HelloThereThanksForTryingMyKata"

" Hello World " => "#HelloWorld"
"""
import unittest


class TestHashTagItMethod(unittest.TestCase):

    def test_text(self):
        self.assertEqual(hashTagIt("Samuel spelar spel"), "#SamuelSpelarSpel")

    def test_EmptyTextReturnsFalse(self):
        self.assertEqual(hashTagIt(""), "false")

    def test_StartsWithHashTag(self):
        self.assertEqual(hashTagIt("SamuelSpelarSpel")[0], "#")

    def test_TextIsShorterThan140Chars(self):
        self.assertEqual(hashTagIt("GHfrrkldflkjrekmlkmldskjflrkjhjfjhdgfjhgdjfhgdjshgferwubmnbcvmzxnblkjlkjrltkjlkjlxsi8lklkdfjlkjrtilkdjfnlsdkjlkjrlkjlskjlkgjrelkjsdlkfjlkjtlkjslkjglkejlkgjsldkjg"), "false")



def hashTagIt(text):
    finalWord = ''

    if ( len(text) > 140 ) or (len(text) == 0 ):
        finalWord = "false"
    else:
        words = text.split()
        for word in words:
            for i in range(len(word)):
                if (i == 0):
                    finalWord = finalWord + word[i].upper()
                else:
                    finalWord = finalWord + word[i]

        finalWord = "#" + finalWord
    return finalWord

def main():
    print("Text")
    

if __name__ == "__main__":
    unittest.main()
    #main()