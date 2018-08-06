'''
Author: Viswas
Date: 3 Aug 2018
Encoding: UTF-8
'''
def main():
    """ This function computes
    the square root of a given number"""
    num = input()
    epsilon = 0.01
    low_low = 0
    high_high = int(num)
    ans = (high_high + low_low) / 2.0
    while abs(ans ** 2 - int(num)) >= epsilon:
        if ans ** 2 < int(num):
            low_low = ans
        else:
            high_high = ans
        ans = (low_low + high_high) / 2.0
    print(ans)
if __name__ == "__main__":
    main()
