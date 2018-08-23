def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result=[]
    for i in range(len(matrix_1)):
    # iterate through columns of Y
        for j in range(len(matrix_2[0])):
        # iterate through rows of Y
            for k in range(len(matrix_2)):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result            

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = []
    result = [[matrix_1[i][j] + matrix_2[i][j]  for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
    return result
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    pass

def main():
    # read matrix 1
    nn_matrix = input().split()
    total_cells =  len(nn_matrix)
    row_cells = int(total_cells**0.5)
    matrix_1 = [nn_matrix[i:i+row_cells] for i in range(0, total_cells, row_cells)]

    # read matrix 2
    nn_matrix = input().split()
    total_cells =  len(nn_matrix)
    row_cells = int(total_cells**0.5)
    matrix_2 = [nn_matrix[i:i+row_cells] for i in range(0, total_cells, row_cells)]


    # add matrix 1 and matrix 2
    add_mat = add_matrix(matrix_1, matrix_2)

    # multiply matrix 1 and matrix 2
    mul_mat = mult_matrix(matrix_1, matrix_2)

if __name__ == '__main__':
    main()
