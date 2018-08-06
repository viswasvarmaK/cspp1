'''
Author: Pranav Surampudi
Date: 3 Aug 2018
Encoding: UTF-8
'''
def main():
    """ This function computes
    the square root of a given number"""
    num = input()
    epsilon = 0.01
    low_l = 0
    high_h = int(num)
    ans = (high_h + low_l) / 2.0
    while abs(ans ** 2 - int(num)) >= epsilon:
        if ans ** 2 < int(num):
            low_l = ans
        else:
            high_h = ans
        ans = (low_l + high_h) / 2.0
    print(ans)
if __name__ == "__main__":
    main()
