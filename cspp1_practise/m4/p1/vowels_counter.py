'''
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

Author:VISWAS

Date:2-8-2018
'''
S =input()
COUNT = 0
for i in S:
    if i in('a','e','i','o','u'):
	    COUNT = COUNT + 1
print(COUNT)	


	
