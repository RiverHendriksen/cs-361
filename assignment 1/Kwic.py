#River Hendriksen 2016
#CS-361 Assignment 1
#Kwic1.py
#This refactors and adds code to make for the more complex function where the string is now split by lines and words
#Kwic0.py is still relevent but edited heavily to accomodate more features

import copy
from copy import deepcopy


#function that works off of the if statement "\n" it would have worked within the elif where .isspace=False but the function involves lists
#and I am too tired to fix it at the moment, maybe see what happens in Kwic2.py maybe i will change it, that is for future me to find out
def wordsplits(x1):
	x2 = []								#I don't believe in global variables so here is x2 again since it serves the same purpose as in Kwic
	for line in x1:						#parses through the list
		x2 += line.split(" ")			#splits the words based on spaces
	x2 = filter(lambda c:c != '', x2)	#based on Alex Groce's comment on canvas I modified it to filter out '' items in the list
	return x2;	
							#return the final value back to Kwic
def deepercopy(x2):
	newList = []
	#for i in range(0,len(x2)):
	newList.append(x2)
	#print newList
	return newList

def circshift(x2,x3):

	for i in range(0,len(x2)):
		x2.append(x2[0])
		del x2[0]
		x3.append(x2[:])
	return x3

def tupleheck(x3,n,i):

	for j in range(len(x3)):
		if len(n) == 0:
			thattuple = (x3[j], )
			thattuple2 = (i, )
			thattuple3 = thattuple + thattuple2
			n.append(thattuple3)
		elif len(n[j-1]) == 2:
			thattuple = (x3[j], )
			thattuple2 = (i, )
			thattuple3 = thattuple + thattuple2
			n.append(thattuple3)
	return n

def try_to_ignore_me(sorted_by_first, ignoreWords):
	#create ironic list name  
	ignore_perfection = []	

	#first for loop, the range of the length of ignorewords (aka how many words did you say to ignore) iterates through it
	for i in range(len(ignoreWords)):

		#second for loop, the range of the length of the sorted tuple list iterates throught it 						
		for x in range(len(sorted_by_first)):

			#referenced from: http://stackoverflow.com/questions/16050952/how-to-remove-all-the-punctuation-in-a-string-python
			#creates a new string without punctuation
			out = "".join(c for c in sorted_by_first[x][0][0] if c not in ('.', '?', ',', '!', ':')) 

			#if the sorted list at the current iteration of the tuple at the list at the first string of the list is equal to the value of ignoreword
			if(out.lower() == ignoreWords[i].lower()):
				#checks to see if ignore_perfection is empty
				if(ignore_perfection == []):
					#copys sorted perfection in the append way, had to do this because otherwise we would be editing the list that we are iterating through
					#and that is a big fat mistake
					ignore_perfection += sorted_by_first
				#removes the tuple if the words match
				ignore_perfection.remove(sorted_by_first[x])

	#if there was an ignore in the function but nothing matches we just return sorted by first
	if(ignore_perfection == []):
		return sorted_by_first
	return ignore_perfection

def handling_list_input(i,j,sorted_by_first, temp, sad, x, ill):
	#needs: run the test again but ignore the same combo of words

	goodbye = False
	pluck1 = 0
	pluck2 = 0
	death = [] 
	while(x != len(sorted_by_first[i][0]) and goodbye == False):
		print "bluck"
		print sorted_by_first[i][0][x]
		print sorted_by_first[j][0]
		print x
		test = False

		out1 = "".join(c for c in sorted_by_first[i][0][x] if c not in ('.', '?', ',', '!', ':')) 
		out1 = out1.lower()
		print "out1 test"
		out2 = []
		death = deepcopy(sorted_by_first[j][0])
		print death
		print range(0, len(death))
		for b in range(0, len(death)):
			out2.append("".join(c for c in death[b] if c not in ('.', '?', ',', '!', ':')) )
			out2[b] = (out2[b].lower())
		 	print out2[b]
		print out2

		if any(out1 in s for s in out2):
			a = (out1, )
			if(len(temp) == 2 ):
				tempoftemp = temp[0]
				print "tempoftemp"
				print tempoftemp
				temp = ()
				temp += (tempoftemp, )
				temp += a
				print "revised temp"
				print temp
			else:
				print"old temp"
				temp+=a
				print temp
		elif (len(temp) == 2):
			while not any(out1 in s for s in out2):
				print x
				print "we doing ok"
				print len(sorted_by_first[i][0])
				if(x+1 == len(sorted_by_first[i][0])):
					print "sorry"
					return 
				x+=1
				out1 = "".join(c for c in sorted_by_first[i][0][x] if c not in ('.', '?', ',', '!', ':'))
			a = (out1, )
			tempoftemp = temp[0]
			print tempoftemp
			temp = ()
			temp += (tempoftemp, )
			temp += a
			print "hells final answer"
			print temp

		if (len(temp) == 2 and temp[0] != temp[1]):

			# if the line pair in temp already exists in sad then we add to the count
			if sad == []:						
				thattuple = (deepcopy(temp), )
				thattuple2 = (2, )
				thattuple3 = thattuple + thattuple2
				sad.append(thattuple3)
				test = True
				print "the illest"
				thattuple4 = (sorted_by_first[i][1], )
				thattuple5 = (sorted_by_first[j][1], )
				thattuple6 = thattuple + thattuple4 + thattuple5
				ill.append(thattuple6)
				print ill
				print "first attempt at sadness"
				print sad

			elif range(len(sad)) == [0] and (any(temp[0] in s for s in sad[0][0])) and (any(temp[1] in s for s in sad[0][0])):
				for item in ill:
					if temp == item[0]:
						pluck1 = item[1]
						pluck2 = item[2]
				print "plucks"
				print pluck1
				print pluck2

				if(sorted_by_first[i][1] != pluck1 and sorted_by_first[j][1] != pluck2):
					newsad = list(sad[0])
					old_count = newsad[1]
					print "this is teh new list"
					print newsad
					print old_count
					old_count += 1
					newsad[1] = old_count
					sad[0] = tuple(newsad)	

			for p in range(len(sad)):
				print "death is coming"
				print  range(len(sad))
							#print sad[p]
				if (any(temp[0] in s for s in sad[p][0])) and (any(temp[1] in s for s in sad[p][0])) and test != True:
					for item in ill:
						print item[0]
						print item[0]
						if(sorted_by_first[i][1] != item[1] and sorted_by_first[j][1] != item[2] or temp != item[0]):
							newsad = list(sad[p])
							old_count = newsad[1]
							old_count += 1
							newsad[1] = old_count
							sad[p] = tuple(newsad)
							print "death wish sadness"
							print sad
							test = True
							break
					break
				else: 
					print "not a match the first time"
			if test == False:
				for item in ill:
					print item[0]
					print item[0]
					if(sorted_by_first[i][1] != item[1] and sorted_by_first[j][1] != item[2] or temp != item[0]):
						print "this is p"
						thattuple = (deepcopy(temp), )
						thattuple2 = (2, )
						thattuple3 = thattuple + thattuple2
						sad.append(thattuple3)
						print "first attempt at sadness: one more time"
						print sad

		x+=1


	print "break"
	return 

def getting_index(sorted_by_first, j, count1):
	for item in sorted_by_first:
		if count1 == item[1]:
			print "this is the index"
			j = sorted_by_first.index(item)
			print j
			return j 
	return


def listpairheck(sorted_by_first):
	#never tested to see if the first one has any duplicates 
	sad =[]
	ill = []
	count1  = 1 
	count2 = 1
	j = 0 
	i=0
	x = 0
	goodbye = False
	finalfantasygoodbye = False
	if range(len(sorted_by_first)) <= 0:
		return sorted_by_first
	#issue: j is sorting through for 5 iterations because of circ shift and sorting, whatever, but it is an issue with the counting 
	#eg the index counting is th problem
	while(i != len(sorted_by_first) and finalfantasygoodbye== False):
		print "this is i:"
		print i
		goodbye = False
		x = 0 
		while(j <= len(sorted_by_first) and goodbye == False):
			print "this is j"
			print j
			temp = ()
			print sorted_by_first
			print len(sorted_by_first)
			print sorted_by_first[-1][1]
			if(sorted_by_first[j][1] == sorted_by_first[i][1] and sorted_by_first[j][1] != sorted_by_first[-1][1]):
				#need to run it once to see if add the first attempt 
				#handling_list_input(i,j,sorted_by_first, temp, sad)
				print "they are equal"
				#This isn't finding the value of the next index it's just incrementing j! I'm dumb. 
				print "god i hope this works"
				j = getting_index(sorted_by_first, j, count1)
				print "j again"
				print j
				count1 +=1
				x = 0
				while(x <= len(sorted_by_first[i][0])):
					handling_list_input(i,j,sorted_by_first, temp, sad, x, ill)
					x+=1
			else:
				if (sorted_by_first[j][1] == sorted_by_first[-1][1]):
					while(x < len(sorted_by_first[i][0])):
						handling_list_input(i,j,sorted_by_first, temp, sad, x, ill)
						x+=1
						print"what is x" 
						print x
						print len(sorted_by_first[i][0])
					print "goodbye"
					break
					goodbye = True
				else:
					j = getting_index(sorted_by_first, j, count1)
					print "the final j"
					count1 += 1
					x = 0
					while(x < len(sorted_by_first[i][0])):
						handling_list_input(i,j,sorted_by_first, temp, sad, x, ill)
						x+=1
						print"what is x" 
						print x
						print len(sorted_by_first[i][0])
							
############################################ j ends
		#run the test again but ignore the same combo of words
		if (sorted_by_first[i][1] == sorted_by_first[-1][1]):
			print "fuckyou"
			finalfantasygoodbye = True 
		else:
			i = getting_index(sorted_by_first, i, count2)
			print "the final "
			count2 += 1
			x = 0
			count1 = sorted_by_first[i][1]+1
			print i
			print count1
			j = 0
			print "this is it two"
			j = getting_index(sorted_by_first, j, count1)
			print j 
			if(j == None):
				break
			print j 
			#while(x != len(sorted_by_first[i][0])):
			#	handling_list_input(i,j,sorted_by_first, temp, sad, x)
			#	x+=1
####################################### i ends
	print sad
	#					thattuple = (deepcopy(temp), )
	#					thattuple2 = (2, )
	#					thattuple3 = thattuple + thattuple2
	#					sad.append(thattuple3)
	tired = []
	undertale = []
	for item in range(len(sad)):
		tired = []
		tired.append(sad[item][1])
		print tired
		tired.append(list(sad[item][0]))
		print tired[1]
		tired[1] = sorted(tired[1])
		print tired
		thattuple = tuple(tired[1], )
		thattuple2 = (tired[0], )
		thattuple = (thattuple, )
		thattuple3 = thattuple + thattuple2
		undertale.append(thattuple3)
		print "yes"
		print undertale
	
	undertale = sorted(undertale, key=lambda tup: tup[0])
	print undertale
	return undertale


#main function`
def Kwic(x1, ignoreWords = [], listPairs = False):
	#print ignoreWords
	x2 = []		#will hold those dank lists
	x3 = []
	n = []
	bewlist = []
	sorted_by_first = []
	Frisk = []
	#blundertale spelled wrong
	bludertale = []
	death2 = ()

	if("\n" in x1):
		x1 = x1.splitlines()	#default function from python to split lines by \n eg. "hello\nbutton" returns ['hello','button']
		for i in range(len(x1)):
			x3 = []
			x2 = []

			bewlist.append(deepercopy(x1[i]))
			x2 = wordsplits(bewlist[i])
			x3 = circshift(x2,x3)
			n = tupleheck(x3,n,i)
		if(listPairs==True):
			Frisk = listpairheck(n)

		print" THIIISSSS ISSS NNNNNNN"
		print n 

		sorted_by_first = sorted(n, key=lambda tup: (tup[0][0].upper(), tup[0][0].islower()))
		#sorted_by_first = sorted(n, key=lambda tup: tup[0].lower())

		print "AHASHSADJASFJJGJADSGJASFGKSAFKH"
		print sorted_by_first

		#print sorted_by_first

		if(ignoreWords != []):
			ignore_perfection = try_to_ignore_me(sorted_by_first, ignoreWords)
			#print "here you "
			#print ignore_perfection
			#return ignore_perfection;


		if(listPairs==True and ignoreWords != []):
			bludertale.append(ignore_perfection)
			bludertale.append(Frisk)
			death2 = tuple(bludertale, )
			print death2
			return death2;

		elif(listPairs==True and ignoreWords == []): 
			bludertale.append(sorted_by_first)
			bludertale.append(Frisk)
			death2 = tuple(bludertale, )
			print death2
			return death2;
		else:
			return sorted_by_first
		
		
		
		

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

		for j in range(len(x3)):	#The lazy mans code, it does the same thing as tupleheck but no longer requires I, if you are curious check tupleheck
			thattuple = (x3[j], )
			thattuple2 = (0,)
			thattuple3 = thattuple + thattuple2
			n.append(thattuple3)

		print" THIIISSSS ISSS NNNNNNN"
		print n 
		sorted_by_first = sorted(n, key=lambda tup: tup[0][0].lower())
		sorted_by_first = sorted(n, key=lambda tup: tup[0])
		print "AHASHSADJASFJJGJADSGJASFGKSAFKH"
		print sorted_by_first
		
		if(ignoreWords != []):
			ignore_perfection = try_to_ignore_me(sorted_by_first, ignoreWords)


		if(listPairs==True and ignoreWords != []):
			bludertale.append(ignore_perfection)
			bludertale.append(Frisk)
			death2 = tuple(bludertale, )
			print death2
			return death2;

		elif(listPairs==True and ignoreWords == []): 
			bludertale.append(sorted_by_first)
			bludertale.append(Frisk)
			death2 = tuple(bludertale, )
			print death2
			return death2;
		else:
			print "deal"
			return sorted_by_first
		return sorted_by_first;

