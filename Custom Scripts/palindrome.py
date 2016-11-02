#This script takes a text file from the Command Line and reads each line to check if it's a palindrome. After confirming, the program prints the line in reverse order.

import sys

file = open(sys.argv[1], "r")  #pass command-line argument to program to read sample.txt file
for line in file:
    line=line.strip()   #removes whitespace characters in strings

    reverseln=line[::-1]   #go through line in reverse order
    sortedln=sorted(line)
    sortedstring="".join(sortedln[::-1])    #concatenate sequence of sortedln strings in reverse order
    if line.lower()==reverseln.lower():     #if the method strings line.lower() equals reverseln.lower() then it is a palindrome
        print('YES | '+sortedstring)     #append string statement to sortedstring variable

    else:
        print('Not a Palindrome | '+sortedstring)
