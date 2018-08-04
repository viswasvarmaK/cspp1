'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
AUTHOR: Viswas
date: 4-8-2018
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
N_N = int(input("enter a number"))
I_I = 0
while I_I < N_N:
    I_I = I_I+1
    if I_I%3 == 0 and I_I%5 == 0:
        print("fizz")
        print('buzz')
    elif I_I%3 == 0:
        print('fizz')
    elif I_I%5 == 0:
        print('buzz')
    else:
        print(I_I)
if __name__ == "__main__":
    main()
