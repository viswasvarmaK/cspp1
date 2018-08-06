''' author: viswas
    date : 06-08-2018
    '''

def paying_debt_off_in_a_year(initial_balance, annual_interest_rate):
    '''
    operation
    '''
    epsilon_val = 0.03
    upper_bound = initial_balance*((1+annual_interest_rate/12.0)**12)/12.0
    mfp_money = 0
    lower_bound = initial_balance/12.0
    # print(lower_bound,upper_bound)
    mir_rate = annual_interest_rate/12.0
    while True:
        # print(mfp)
        ubm = initial_balance
        mfp_money = (lower_bound+upper_bound)/2.0
        # mfp = int(mfp*100)/100.0
        for _ in range(12):
            mub = ubm - mfp_money
            ubm = mub + mir_rate*mub
        if ubm > epsilon_val:
            lower_bound = mfp_money
        elif ubm < -epsilon_val:
            upper_bound = mfp_money
        else:
            break
    # mfp = int(mfp*100)/100.0
    return "Lowest Payment: "+str(round(mfp_money, 2))

def main():
    '''
    main functiion
    '''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_in_a_year(data[0], data[1]))

if __name__ == "__main__":
    main()
