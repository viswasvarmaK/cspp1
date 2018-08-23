'''
Author: Viswas
Date: 23-8-2018
'''
def mult_matrix(m_1, m_2, r_1, r_2, c_1):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if c_1 == r_2:
        multiplication_matrix = []
        for i in range(r_1):
            temp = []
            for j in range(r_1):
                sum_val = 0
                for k in range(c_1):
                    sum_val = sum_val + (m_1[i][k] * m_2[k][j])
                temp.append(sum_val)
            multiplication_matrix.append(temp)
        return multiplication_matrix
    print("Error: Matrix shapes invalid for mult")
    return None #for pylint

def add_matrix(m_1, m_2, r_1, r_2, c_1, c_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if r_1 == r_2 and c_1 == c_2:
        addition_matrix = []
        for i in range(0, r_1):
            temp = []
            for j in range(0, c_1):
                temp.append(m_1[i][j] + m_2[i][j])
            addition_matrix.append(temp)
        return addition_matrix
    print("Error: Matrix shapes invalid for addition")
    return None #for pylint
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    dimensions = input().split(",")
    row_value = int(dimensions[0])
    column_value = int(dimensions[1])
    mat = []
    for i in range(0, row_value):
        mat.append(list(map(int, input().split())))
    flag = True
    for i in mat:
        count = 0
        for _ in i:
            count += 1
        if count != column_value:
            flag = False
    return mat, row_value, column_value, flag

def main():
    # read matrix 1
    # nn_matrix = input().split()
    # total_cells =  len(nn_matrix)
    # row_cells = int(total_cells**0.5)
    # matrix_1 = [nn_matrix[i:i+row_cells] for i in range(0, total_cells, row_cells)]
    # matrix_1 = []
    # matrix_1 = read_matrix(matrix_1)
    # # read matrix 2
    # nn_matrix = input().split()
    # total_cells =  len(nn_matrix)
    # row_cells = int(total_cells**0.5)
    # matrix_2 = [nn_matrix[i:i+row_cells] for i in range(0, total_cells, row_cells)]
    # matrix_2 = []
    # matrix_2 = read_matrix(matrix_2)
    # # add matrix 1 and matrix 2
    # add_mat = add_matrix(matrix_1, matrix_2)
    # # multiply matrix 1 and matrix 2
    # mul_mat = mult_matrix(matrix_1, matrix_2)
    '''main function '''
    (matrix_1, row_1, column_1, flag_1) = read_matrix()

    (matrix_2, row_2, column_2, flag_2) = read_matrix()

    #print(flag_1, flag_2)

    if flag_1 and flag_2:
        print(add_matrix(matrix_1, matrix_2, row_1, row_2, column_1, column_2))
        print(mult_matrix(matrix_1, matrix_2, row_1, row_2, column_1)) #column_2 is also sent

        # print(addition_matrix)
        # print(multiplication_matrix)

    else:
        print("Error: Invalid input for the matrix")
if __name__ == '__main__':
    main()
