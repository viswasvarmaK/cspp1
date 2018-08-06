'''
Author: VISWAS
Date: 6-8-2018
'''

def eval_quadratic(a_a, b_b, c_c, x_x):
    '''function to quadratic equation'''
    s_s = (a_a* (x_x ** 2)) + (b_b*x_x) + c_c
    return s_s

def main():
    ''' main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    k = len(data)
    for x_1 in range(k):
        temp = str(data[x_1]).split('.')
        if temp[1] == '0':
            data[x_1] = int(float(str(data[x_1])))
        else:
            data[x_1] = data[x_1]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
