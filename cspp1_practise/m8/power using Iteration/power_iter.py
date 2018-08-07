'''
# Exercise: PowerIter
Author:VISWAS
Date: 7-8-2018
'''


def iterpower(base_b, exp_e):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    s_s = 1
    for i_i in range(0, exp_e):
        s_s = base_b * s_s
        i_i += 1
    print(s_s)
def main():
    '''
    main function
    '''
    data = input()
    data = data.split()
    print(iterpower(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
