# DNA_to_RNA_Conversion.py
'''
8 kyu
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a funciton which translates a given DNA string into RNA.

For example:

DNAtoRNA("GCAT") returns ("GCAU")
'''

import unittest


class TestDnaToRnaConversion(unittest.TestCase):

    def test_DNAtoRNAWithT(self):
        self.assertEqual(dnaToRna("GCAT"), "GCAU")

    def test_DNAtoRNAToLong(self):
        self.assertEqual(dnaToRna("GCATG"), "Error!")

    def test_DNAtoRNAToShort(self):
        self.assertEqual(dnaToRna("GCA"), "Error!")


    def test_DNAtoRNAWithoutT(self):
        self.assertEqual(dnaToRna("GCAA"), "GCAA")


def dnaToRna(dna):
    returnValue = ''
    if ( len(dna) == 4):
        for index in range(len(dna)):
            if (dna[index] == "T" ):
                returnValue = returnValue + "U"
            else:
                returnValue = returnValue + dna[index]
        return returnValue
    else:
        return "Error!"



def main():
    print("DNA to RNA Conversion")
    



if __name__ == "__main__":
    unittest.main()
    #main()

