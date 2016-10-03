#River Hendriksen 2016
#CS-361 Assignment 1
#Kwic0test.py
#The test will see if the various conditions applied will still allow to the program to work

import Kwic

#basic test to see if implementation of kwic0.py works as expected
test1 = "hello\nThat is cool"
expectedLen = len(filter(lambda c:c == "\n", test1))  #referenced from comment Alex groce made on discussions :-)
#lambda: c exists the line break exists 
#filter: applies to the entire string and creates an array with \n
#len: counts them
#eg lambda c: c!= "\n" would give an array of values when it is not '\n' which would be 17 in test 1
assert len(Kwic.Kwic(test1)) >= expectedLen

#tests 
test2 = ""
assert(Kwic.Kwic(test2)==[])

test3 = " hey \nthis is a test \n\n. weird.... that is crazy"
expectedLen = len(filter(lambda c:c == "\n", test3))  #referenced from comment Alex groce made on discussions :-)
assert len(Kwic.Kwic(test3)) >= expectedLen

test4 = "\n\n\n\n\n\n\n"
assert(Kwic.Kwic(test4)==[])

test5 = "hey budyy"
expectedLen = len(filter(lambda c:c == "\n", test5))  #referenced from comment Alex groce made on discussions :-)
assert len(Kwic.Kwic(test5)) >= expectedLen

test5 = "A a \n Apple bottom JEansS "
expectedLen = len(filter(lambda c:c == "\n", test5))  #referenced from comment Alex groce made on discussions :-)
assert len(Kwic.Kwic(test5)) >= expectedLen
