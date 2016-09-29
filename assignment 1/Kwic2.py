#River Hendriksen 2016
#CS-361 Assignment 1
#Kwic2.py
#This code changes the rules so that now there will be a circular shift that occurs and puts the result in an array of lists that in itself 
#contains an array of strings (confusing sounding) the refactoring of this code was less difficult to modify (although more difficult to code)
#I created two separate functions, one is called within the other that allow the original code resulting from kwic1.py to be parsed 
#and then separated into unique lists, the way I did it may be a little overboard but it works as a result adn can be applied 
#to the if statement and the elif statements if need be. 


#function that works off of the if statement "\n" it would have worked within the elif where .isspace=False but the function involves lists
#and I am too tired to fix it at the moment, maybe see what happens in Kwic2.py maybe i will change it, that is for future me to find out
def wordsplits(x1):
	x2 = []								#I don't believe in global variables so here is x2 again since it serves the same purpose as in Kwic
	for line in x1:						#parses through the list
		x2 += line.split(" ")			#splits the words based on spaces
	x2 = filter(lambda c:c != '', x2)	#based on Alex Groce's comment on canvas I modified it to filter out '' items in the list
	return x2;	
							#return the final value back to Kwic


#although named after the deepcopy function from the copy library of python, this one creates a new list that shares all the values of x2 
#and appends them to new list, this helps since append passes by reference and not by value which was causing issues before.
def deepcopy(x2):
	newList = []
	for i in range(0,len(x2)):
		newList.append(x2[i])
	#print newList
	return newList

#circshift is the main function of circular shift that has deepcopy included within it. it takes in x2 (the main list) and
#x3(the empty list) and switched around the places of the items in the list then calls deepcopy to copy them correctly into multiply different lists
#in the arrayx
def circshift(x2,x3):
	for i in range(0,len(x2)):
		x2.append(x2[0])
		del x2[0]
		x3.append(deepcopy(x2))	
	return x3

#main function
def Kwic(x1):
	x2 = []		#will hold those dank lists
	x3 = []

	if("\n" in x1):
		x1 = x1.splitlines()	#default function from python to split lines by \n eg. "hello\button" returns ['hello','button']
		x2 = wordsplits(x1)		#calls wordsplits at the top, I did it to make kwic look a little nice (just for you)
		x3 = circshift(x2,x3)
		return x3;

	#I realized that .isspace comes out to False is there is an empty string to quote the python method defintion
	#"This method returns true if there are only whitespace characters in the string and there is at least one character, false otherwise."
	#While it still works if .isspace is false I felt like that would be an oversight so I made this dumb or addition so if there is a bunch of white spaces or very little
	#it will still be the empty set
	elif(x1.isspace()==True or x1 == ""):
		x1 = x1.split()		#makes it the right format eg. [] always for this elif
		return x1

	#If there isn't line breaks and no blank entries this is where you wind up, Welcome to the bottom buddy. 
	#it does the same thing as wordsplits but does it for strings rather than lists
	elif(x1.isspace()==False):
		x2 += x1.split(" ")
		x2 = filter(lambda c:c != '', x2)
		x3 = circshift(x2,x3)
		print x3
		return x3;
