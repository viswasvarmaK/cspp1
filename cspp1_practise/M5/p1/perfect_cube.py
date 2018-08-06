'''
Author: Viswas
Date: 3 Aug 2018
Encoding: UTF-8
'''
def main():
    """This fucntion checks whether or not
    a given number is a perfect cube"""
    n_n = int(input())
    t_t = 0
    for i in range(1, n_n + 1, 1):
        if i**3 == n_n:
            t_t += 1
            print(str(n_n) + " is a perfect cube")
            exit()
    if t_t == 0:
        print(str(n_n)+" is not a perfect cube")
if __name__ == "__main__":
    main()
