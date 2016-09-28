#River Hendriksen 2016
#CS-361 Assignment 1
#Kwic0.py splits lines by the new line value ('\n') 
#The test will see if the various conditions applied will still allow to teh program to work

#Kwic takes in one parameter at this point, that param being the "any length" string
def Kwic(x1):
	x1 = x1.splitlines()	#default function from python to split lines by \n eg. "hello\button" returns ['hello','button']
	print x1				#prints results for manual debugging :-)
	x2 = filter(lambda c:c != '', x2)	#based on Alex Groce's comment on canvas I modified it to filter out '' items in the list
	return x1				#return the value from x1.splitlines() to whever the function is called


