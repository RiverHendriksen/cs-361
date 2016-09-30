#River Hendriksen 2016
#CS-361 Assignment 1
#Kwic1test.py
#The test will see if the various conditions applied will still allow to the program to work

#this test runs under the assumption that we are not in a list of lists at this point
#eg the example ("hello \n bucko that ") does prouduces ["hello" , "bucko", "that"] and not [["hello"],["bucko", "that"]]
#This comes from a misunderstanding of the assignments boundaries when I first started this assignment (I am writing this as i have finished the assignment)
#this problem is solved within kwic3.py and has tuples as well. This test and the program kwic1.py are not wrong for this reason
#as this is TDD my program passed my tests based on the assumptions that made since alex groce said this assignment is open to interpertation

import Kwic

#basic test to see if implementation of kwic works correctly 
test1 = "hello that is cool"
expectedLen = len(filter(lambda c:c == "\n", test1))  #referenced from comment Alex groce made on discussions :-)
#lambda: c exists the line break exists 
#filter: applies to the entire string and creates an array with \n
#len: counts them
#Since this now has to break up the words into individual space this will result in a value of at least that must be true for this test to pass
assert len(Kwic.Kwic(test1)) >= expectedLen

#classic assert to make sure the empty set is empty tests the elif for if x==""
test2 = ""
assert(Kwic.Kwic(test2)==[])

#Tests for spaces to see if something weird happens, answer is it doesn't covers the test if .isspace is is False
test3 = "woah  oh oh        yeah"
print Kwic.Kwic(test3)
expectedLen = 4
assert len(Kwic.Kwic(test3)) >= expectedLen

#Tests the large empty set more double checking .isspace
test4 = "         " 
assert(Kwic.Kwic(test4)==[])

test5 = "hey hey \n this is not the way \n back"


