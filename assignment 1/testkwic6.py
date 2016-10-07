import Kwic

#basic test to see if implementation of kwic0.py works as expected

#first test to get it running with one instance of two wors and two lines 
test1 = "hello cool is \n That is cool"
expectedLen = len(filter(lambda c:c == "\n", test1))  #referenced from comment Alex groce made on discussions :-)

#test4 = "that is cool butt \n that is cool"
#assert len(Kwic.Kwic(test4)) >= expectedLen

test5 = "that is cool butt \n that is like cool \n cool like is "
assert len(Kwic.Kwic(test5)) >= expectedLen



print "########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################"


#test punctuation
test6 = "that is co!ol butt \n that is like cool \n cool like is "
assert len(Kwic.Kwic(test6)) >= expectedLen

print "########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################"

#test capitals 
test7 = "that is Co!oL butt \n that iS like cool \n cool like is "
assert len(Kwic.Kwic(test7)) >= expectedLen

#test the empty set
test8 = '\n'  
assert len(Kwic.Kwic(test8, listPairs = True)) >= expectedLen

#test when ignore words and listpairs is true
test8 = '\n'  
assert len(Kwic.Kwic(test8, listPairs = True)) >= expectedLen


#if ignore words and list pairs are active
test9 = "that is co!ol butt \n that is like cool \n cool like is "
assert len(Kwic.Kwic(test9, ignoreWords = ['is'], listPairs = True)) >= expectedLen

#no backspace
test10 = "that is co!ol butt cool like is "
assert len(Kwic.Kwic(test10, ignoreWords = ['is'], listPairs = True)) >= expectedLen

#add to other Kwic and maybe test7 style 
assert Kwic.Kwic("hello here, hello there, hello everywhere",listPairs = True) == ([(['everywhere', 'hello', 'here,', 'hello', 'there,', 'hello'], 0), (['hello', 'everywhere', 'hello', 'here,', 'hello', 'there,'], 0), (['hello', 'here,', 'hello', 'there,', 'hello', 'everywhere'], 0), (['hello', 'there,', 'hello', 'everywhere', 'hello', 'here,'], 0), (['here,', 'hello', 'there,', 'hello', 'everywhere', 'hello'], 0), (['there,', 'hello', 'everywhere', 'hello', 'here,', 'hello'], 0)], [])

'''assert len(Kwic.Kwic(test1)) >= expectedLen
#basic test to see if implementation of kwic0.py works as expected
#caught errors with more than two indexs created an infinite for loop
test2 = "hello cool is \n That is cool \n that is \n cool"
expectedLen = len(filter(lambda c:c == "\n", test1))  #referenced from comment Alex groce made on discussions :-)
#lambda: c exists the line break exists 
#filter: applies to the entire string and creates an array with \n
#len: counts them
#eg lambda c: c!= "\n" would give an array of values when it is not '\n' which would be 17 in test 1
assert len(Kwic.Kwic(test2)) >= expectedLen

#three variable test
test3 = "hello cool is \n That is cool \n that is \n  is cool"
assert len(Kwic.Kwic(test3)) >= expectedLen

#same variables
test4 = "hello hello \n hello hello"
assert len(Kwic.Kwic(test4)) >= expectedLen

#test5 = "hello hello cool is \n hello hello cool is"
#assert len(Kwic.Kwic(test5)) >= expectedLen

#two different variables
test4 = "that is cool butt \n that is cool"
assert len(Kwic.Kwic(test4)) >= expectedLen'''
