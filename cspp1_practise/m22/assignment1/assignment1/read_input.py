'''
Write a python program to read multiple lines of text input and store the input into a string.
Author: Viswas
Date : 25-8-2018
'''
def main():
    '''
    main function
    '''
    str_1 = ''
    input_1 = int(input())
    for _ in range(input_1):
        input_2 = input()
        str_1 = input_2
        print(str_1)
if __name__ == '__main__':
    main()
