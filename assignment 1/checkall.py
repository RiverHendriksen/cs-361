from Kwic import *
from pprint import pprint

for l in open("tocheck.txt"):
    print "="*50
    input = l[:-1]
    print "INPUT:",input
    v = eval("Kwic("+input+")")
    print "OUTPUT:"
    pprint(v)
    print
    
