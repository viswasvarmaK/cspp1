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
   

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
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
