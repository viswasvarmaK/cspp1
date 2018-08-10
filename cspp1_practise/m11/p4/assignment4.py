'''
#Exercise: Assignment-4
Author: Viswas
Date : 10-8-2018
'''
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand:dictionary (string int)
    returns: integer
    """
    # TO DO... <--Remove this comment when you code this function
    s_s = 0
    for i in hand.values():
        s_s = s_s + i
    return s_s
def main():
    '''
    Main function
    '''
    n_n = input()
    adict_a = {}
    for i in range(int(n_n)):
        data = input()
        l_1 = data.split()
        i += 1#this line is written only for pylint compliance
        adict_a[l_1[0]] = int(l_1[1])
    print(calculate_handlen(adict_a))
if __name__ == "__main__":
    main()
