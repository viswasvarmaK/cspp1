'''
# Exercise: Is In
Author: Viswas
Date: 7-8-2018
'''
def is_in(char, input_s):
    global low
    global high 
    global middle
    middle = (low + high)//2
    if low == high:
        return False
    if input_s[middle] == char:
        return True
    if input_s[middle] > char:
        high = middle-1
        return is_in(char, input_s)
    if input_s[middle] < char:
        low = middle+1
        return is_in(char, input_s)
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
   

def main():
    data = input()
    data_1 = input()
    if data_1 == "":
        return print("False")
    else:
        string_sort = sorted(data_1)
        string_sort = ''.join(string_sort)
        global low
        global high 
        global middle
        low = 0
        high = len(data_1)
        print(is_in(data, string_sort))
if __name__ == "__main__":
    main()

   