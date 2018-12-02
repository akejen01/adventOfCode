# test.py

"""

"""

text = "this is a text"


words = text.split(" ")

finalWord = ""

for word in words:

    for i in range(len(word)):
        if (i == 0):
            finalWord = finalWord + word[i].upper()
        else:
            finalWord = finalWord + word[i]

finalWord = "#" + finalWord
print(finalWord)
print("\nDone!")