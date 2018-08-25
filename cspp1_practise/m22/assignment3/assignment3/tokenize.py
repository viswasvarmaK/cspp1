'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dict = {}
    str_1 = string
    str_1 = str_1.split(" ")
    for i in range(str_1):
        print(i)
        if i not in dict:
            d[i] += 1
        else:
           # dict.update('i':1)
    return string
def main():
    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
