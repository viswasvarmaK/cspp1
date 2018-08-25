'''
#Write a function to clean up a given string by removing the special characters and retain
#alphabets in both upper and lower case and numbers.
Author : viswas
Date: 25-8-2018
'''
def clean_string(string):
    '''
    sun function
    '''
    str_1 = ""
    for char in string:
        if char in "!@#$%^&*() .":
        else:
            str_1 += char
    return str_1
def main():
    '''
    main function
    '''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
