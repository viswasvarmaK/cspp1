'''
Author: Viswas
Date: 3 August 2018
Encoding: UTF-8
'''
def main():
    """This function prints the number
    that the user has guessed """
    max_max = 100
    min_min = 0
    c_h = ''
    while c_h != 'c':
        guess_a = (min_min + max_max)// 2
        print("is your guess "+ str(guess_num))
        c_h = input("Enter your choice: ")
        if c_h == 'l':
            min_min = guess_num
        else:
            max_max = guess_num
    print("The number you guessed is "+ str(guess_num))


if __name__ == "__main__":
    main()
