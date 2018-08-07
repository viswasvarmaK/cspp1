'''
# Exercise: Assignment-2
Author : Viswas
Date: 7-8-2018
'''

def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n == 0:
        return 0
    return (n % 10) + sumofdigits(n // 10)
    pass

def main():
    a = input()
    print(sumofdigits(int(a)))  

if __name__== "__main__":
    main()
