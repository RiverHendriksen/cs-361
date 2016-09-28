#River Hendriksen 2016
#CS-361 Assignment 1
#Kwic0test.py
#The test will see if the various conditions applied will still allow to the program to work

import Kwic

#basic test to see if implementation of kwic works correctly 
test1 = "hello that is cool"
assert(Kwic.Kwic(test1)==["hello", "that" ,"is", "cool"])

test2 = ""
assert(Kwic.Kwic(test2)==[])

test3 = "woah  oh oh        yeah"
print Kwic.Kwic(test3)
assert(Kwic.Kwic(test3)==["woah","oh","oh","yeah"])

