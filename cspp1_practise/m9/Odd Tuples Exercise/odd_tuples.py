#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddtuples(atup_1):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    sum=()
    for i in range(0, len(atup_1)+1, 2):
    	sum += (atup_1[i],)
    return sum

def main():
    data = input()
    data = data.split()
    atup_1=()
    for j in range(len(data)):
        atup_1 += ((data[j]),)
    print(oddtuples(atup_1))
        

if __name__ == "__main__":
    main()
