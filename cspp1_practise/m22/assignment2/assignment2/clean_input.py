'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    str_1 = string
    for i in str_1:
        if str_1.translate('', '!'):
        if str_1.translate('', '@'):
        if str_1.translate('', '#'):
        if str_1.translate('', '$'):
        if str_1.translate('', '%'):    
        if str_1.translate('', '^'):
        if str_1.translate('', '&'):
        if str_1.translate('', '*'):
        if str_1.translate('', '('):
        if str_1.translate('', ')'):
        if str_1.translate('', ' '):    

    return str_1    
    # for char in string:
    #     if char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '*' or char == '(' or char == ')' or char == ' ':
    #         removed = original.replace("!@#$%^&*()", "")
    #     else:
    #         str_1.append(char)    
    # return str_1
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
