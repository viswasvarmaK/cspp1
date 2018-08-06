'''
# Assignment-2 - Paying Debt off in a Year

Author:VISWAS
Date: 6-8-2018
'''

def paying_debt_off_in_a_year(initial_balance, annual_interest_rate):
    ''' function
    '''
    mfp = 0
    while True:
        ubm = initial_balance
        for _ in range(12):
            mir = annual_interest_rate/12.0
            mub = ubm - mfp
            ubm = mub + mir*mub
        # print(mfp)
        if ubm <= 0:
            break
        mfp += 10
    return "Lowest Payment: "+str(mfp)

def main():
    """
    main function
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_in_a_year(data[0], data[1]))

if __name__ == "__main__":
    main()
