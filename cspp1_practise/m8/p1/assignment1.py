'''
# Exercise: Assignment-1
Author: Viswas
Date: 7-8-2018
'''
def factorial(n_1):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_1 in (1, 0):
        return 1
    return n_1*factorial(n_1-1)
def main():
    '''
    MAIN FUNCTION
    '''
    a_1 = input()
    print(factorial(int(a_1)))

if __name__ == "__main__":
    main()
