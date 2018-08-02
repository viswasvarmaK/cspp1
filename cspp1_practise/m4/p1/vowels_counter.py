#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	count=0
	s = raw_input("azcbobobegghaki")
	for i in s:
	    if char('a','e','i','o','u'):
	    	count=count+1
print(count)	    	

	
