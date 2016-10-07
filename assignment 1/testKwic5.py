#River Hendriksen 2016
#CS-361 Assignment 1
#Kwic0test.py
#The test will see if the various conditions applied will still allow to the program to work

import Kwic

test1 = "b!ut \n !!don't go"
Kwic.Kwic(test1, ignoreWords = ["but"])
Kwic.Kwic(test1, ignoreWords = ["but"])
Kwic.Kwic("?!go!!!od morning-!", ignoreWords = ['!GoOd'])
#basic test to see if implementation of kwic0.py works as expected
'''test1 = "hello\nThat is cool ok."
expectedLen = len(filter(lambda c:c == "\n", test1))  #referenced from comment Alex groce made on discussions :-) 
#lambda: c exists the line break exists 
#filter: applies to the entire string and creates an array with \n
#len: counts them
#eg lambda c: c!= "\n" would give an array of values when it is not '\n' which would be 17 in test 1
Kwic.Kwic(test1, ignoreWords = ["is"])
Kwic.Kwic(test1, ignoreWords = ["is","That"])
Kwic.Kwic(test1, ignoreWords = ["is","that"])
Kwic.Kwic(test1, ignoreWords = ["is","that","ok"])
Kwic.Kwic(test1, ignoreWords = ["is","that","ok."])
print Kwic.Kwic(test1)





#assert len(Kwic.Kwic(test1)) >= expectedLen
test2 = "hello\nThat is cool fun "
Kwic.Kwic(test2, ignoreWords = ["is","That" , "fun"]) 	#there is no fun

test3 = "fuck me softly"
Kwic.Kwic(test3, ignoreWords = ["softly"]) 	#there is fun now
#print Kwic.Kwic(test3)'''




