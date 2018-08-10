'''
# Assignment-3
Author: Viswas
Date : 10-8-2018

'''

def isValidWord(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

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
        for char in word_list:
            if word in word_list:
                return True
    return False
def main():
    word=input()
    n=int(input())
    adict={}
    for i in range(n):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    l2=input().split()
    print(isValidWord(word,adict,l2))
        


if __name__== "__main__":
    main()