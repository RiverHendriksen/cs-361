
import Kwic

#tests for no period if function still works
test1 = "hello cool is \n That is cool"
expectedLen = len(filter(lambda c:c == "\n", test1))  #referenced from comment Alex groce made on discussions :-)
assert len(Kwic.Kwic(test1, periodsToBreaks = True)) >= expectedLen

#test to see if the two tests are the same
test2 = "hello cool is. That. is cool"
print(Kwic.Kwic(test2, periodsToBreaks = True))

print(Kwic.Kwic("Hello there.\nHello there, buddy.\nHello and goodbye, buddy.\nHello is like buddy Goodbye!", listPairs=True))
#print(Kwic.Kwic ("Hello there.  Hello there, buddy.    Hello and goodbye, buddy. Hello is like buddy Goodbye!", listPairs=True, periodsToBreaks=True))