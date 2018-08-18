'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = str(dict1)
    dict2 = str(dict2)
    dict1 = dict1.lower()
    dict2 = dict2.lower()
    dict1 = dict1.strip()
    dict2 = dict2.strip()
    dict1 = dict1.split(" ")
    dict2 = dict1.split(" ")
    
    for char in dict1:
    	if char in "@!#$%^&*():;":
    		dict1.remove(char)
    		char = ""
    		dict1 = dict1.strip()
    for char in dict2:
        if char "@!#$%^&*():;":
            dict2.remove(char)
            char = ""
            dict2 = dict2.strip()

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    import stopwords.txt
    
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
