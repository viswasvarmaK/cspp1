'''
# Exercise: PowerRecr
AUTHOR : VISWAS
Date : 7-8-2018
'''
def recurpower(base, exp):
    '''
    called function
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    if exp == 1:
        return base*1
    return base * recurpower(base, exp-1)
def main():
    '''
    MAIN FUNCTION
    '''
    data = input()
    data = data.split()
    print(recurpower(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
