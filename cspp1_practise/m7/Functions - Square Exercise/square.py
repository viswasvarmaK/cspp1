'''
# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.

# This function takes in one number and returns one number.
Author: VISWAS
Date: 6-8-2018
'''

def square(x_num):
    '''
    x: int or float.
    '''
    return x_num ** 2

def main():
    '''
    This is main function
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
