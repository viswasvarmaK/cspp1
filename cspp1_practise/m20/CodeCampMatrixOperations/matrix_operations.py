'''
Author: Viswas
Date: 23-8-2018
'''
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[0 for j in range(len(m2[0]))] for _ in range(len(m1))]
    if len(m1[0]) == len(m2):
    	for i in range(len(m1)):
    		for j in range(len(m2[0])):
    			for j in range(len(m2)):
    				result[i][j] += int(m1[i][k] * int(m2[k][j]))
    	return result
    else:
        print("error: Matrix shapes invalid for mult")
        return None				


def add_matrix(m1, m2):
	''''''
	if(len(m1)) == len(m2) and len(m1[0] == len(m2[0])):
		result = []
		for i in range(len(m1)):
			sample = []
			for j in range(len(m2)):
				sample.append(int(m1[j]) + int(m2[j])
			result.append(sample)
			
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    input_row_col = input().split(" ")
    rows = int(input_row_col[0])
    print(rows)
    columns = int(input_row_col[1])
    print(columns)
    matrix = []
    for i in range(rows):
    	matrix.append(input().split(" "))
    return matrix	
def main():
    # read matrix 1
    m1 = read_matrix()
    print(m1)
    # # read matrix 2
    m2 = read_matrix()
    print(m2)
    # # add matrix 1 and matrix 2
    print(add_matrix(m1, m2))
    # # multiply matrix 1 and matrix 2
    print(mult_matrix(m1, m2))   
if __name__ == '__main__':
    main()
