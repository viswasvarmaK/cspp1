''' author : viswas
    date : 06-08-2018'''
def odd(x_1):
    '''odd function
    '''
    return x_1 % 2 != 0

def main():
    ''' main fun
    '''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
