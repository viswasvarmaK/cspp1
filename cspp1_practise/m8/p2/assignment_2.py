'''
# Exercise: Assignment2
Author : Viswas
Date: 7-8-2018
'''

def sum_ofdigits(n_1):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_1 == 0:
        return 0
    return (n_1 % 10) + sum_ofdigits(n_1 // 10)
def main():
    '''Main Function
    '''
    a_1 = input()
    print(sum_ofdigits(int(a_1)))
if __name__ == "__main__":
    main()
