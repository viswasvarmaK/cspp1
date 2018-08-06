''' author : viswas
    date : 06-08-2018
    '''
def square(x_1):
    ''' square
    '''
    return (x_1)**2

def fourthpower(x_1):
    ''' fourth power
    '''
    return square(x_1)**2

def main():
    '''main function
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthpower(int(float(str(data)))))
    else:
        print(fourthpower(data))

if __name__ == "__main__":
    main()
