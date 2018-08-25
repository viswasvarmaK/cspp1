'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    str_1 = string
    ''.join(e for e in str_1 if e.isalnum())
    # for i in str_1:
    #     if i == '!':
    #         str_1.translate(None, '!')   
    #     if i == '@':
    #         str_1.translate(None, '@')
    #     if i == '#':
    #         str_1.translate(None, '#')
    #     if i == '$':
    #         str_1.translate(None, '$')
    #     if i == '%':
    #         str_1.translate(None, '%')
    #     if i == '^':
    #         str_1.translate(None, '^')
    #     if i == '&':
    #         str_1.translate(None, '&')
    #     if i == '*':
    #         str_1.translate(None, '*')
    #     if i == '(':
    #         str_1.translate(None, '(')
    #     if i == ')':
    #         str_1.translate(None, ')')
    #     if i == ' ':
    #         str_1.translate(None, ' ')


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
