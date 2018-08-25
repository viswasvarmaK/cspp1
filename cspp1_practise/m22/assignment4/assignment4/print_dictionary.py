'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    sub fun
    '''
    sort_1 = sorted(dictionary)
    for _ in sort_1:
        print(i+" "+"-"+" "+str(dictionary[i]))

def main():
    '''
    main fun
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
