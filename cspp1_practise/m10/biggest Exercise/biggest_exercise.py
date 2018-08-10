#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values  associated with it
    '''
    # Your Code Here
    values_v=list(aDict.values())
    max_value= len(values_v[0])
    keys_k=list(aDict.keys())
    max_key= keys_k[0]
    for i in aDict:
        if len(aDict[i]) > max_value:
            max_value = len(aDict[i])
            max_key = i
    return max_key        

    

def main():
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(biggest(aDict))


if __name__== "__main__":
    main()