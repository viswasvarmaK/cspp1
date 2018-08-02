'''
author: viswas
date : 2/8/18
'''

def main():
    '''main function'''
    s_str = input()
    # the input string is in s
    # remove pass and start your code here
    count_s = 0
    for i_1 in s_str:
        if i_1 in ('a', 'e', 'i', 'o', 'u'):
            count_s = count_s + 1
    print(count_s)

if __name__ == "__main__":
    main()
