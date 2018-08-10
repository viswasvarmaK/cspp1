'''
#Exercise: Assignment-2
Author: Viswas
Date : 10-8-2018
'''

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    word = list(word)
    for i in word:
        if i in list(hand.keys()):
            hand[i] -= 1
    return hand
def main():
    '''
    Main document
    '''
    n_n = input()
    adict = {}
    for i in range(int(n_n)):
        i = i+1
        data = input()
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
    data1 = input()
    print(update_hand(adict, data1))

if __name__ == "__main__":
    main()
