'''
# Assignment-3
Author: Viswas
Date : 10-8-2018

'''

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False
    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    count = 0
    len_1 = len(word)
    for i in word:
        if i in hand:
            count += 1
    if count == len_1:
        for i in range(len(word_list)):
            if word in word_list:
                return True
    return False
def main():
    """
    main function
    """
    word = input()
    n_n = int(input())
    adict = {}
    for i in range(n_n):
        i += 1#for pilint
        data = input()
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
    l_2 = input().split()
    print(is_valid_word(word, adict,l_2))
if __name__ == "__main__":
    main()
