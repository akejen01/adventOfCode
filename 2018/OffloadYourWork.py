# HashTagGenerator
"""
7 kyu
You are the best freelancer in the city. Everybody knows you, but what they don't know, is that you are actually offloading your work to other freelancers and and you rarely need to do any work. You're living the life!

To make this process easier you need to write a method called workNeeded to figure out how much time you need to contribute to a project.

Giving the amount of time in minutes needed to complete the project and an array of pair values representing other freelancers' time in [Hours, Minutes] format ie. [[2, 33], [3, 44]] calculate how much time you will need to contribute to the project (if at all) and return a string depending on the case.

    If we need to contribute time to the project then return "I need to work x hour(s) and y minute(s)"
    If we don't have to contribute any time to the project then return "Easy Money!"

"""
import unittest
from datetime import datetime, timedelta


class TestHashTagItMethod(unittest.TestCase):

    def test_workNeeded1(self):
        self.assertEqual(workNeeded(300, [[3,0],[4,10]]), "Easy Money!")

    def test_workNeeded2(self):
        self.assertEqual(workNeeded(1000, [[3,0],[4,10]]), "I need to work 9 hour(s) and 30 minute(s)")




def workNeeded(timeToCompleteWork, freelancers ):
    totalTimeByFreelancers = 0
    
    for freelancer in freelancers:
        totalTimeByFreelancers += freelancer[0] * 60 + freelancer[1]

    if (totalTimeByFreelancers >= timeToCompleteWork):
        return "Easy Money!"
    else:
        t = timeToCompleteWork - totalTimeByFreelancers
                
        return "I need to work " +str(t/60)+ " hour(s) and "+ str(t%60)+" minute(s)" 

def main():
    print("Text")
    

if __name__ == "__main__":
    unittest.main()
    #main()