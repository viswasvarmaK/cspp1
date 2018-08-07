'''
# Exercise: Assignment-1
Author: Viswas
Date: 7-8-2018
'''


def factorial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n in (1, 0):
        return 1
    return n*factorial(n-1)
    


def main():
    a = input()
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
