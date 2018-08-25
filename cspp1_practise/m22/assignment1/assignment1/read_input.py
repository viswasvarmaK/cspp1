'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    # no_of_lines = input().split(" ")
    # lines = ""
    # for i in range(no_of_lines):
    #     lines += input() + "\n"
    # print(lines)
    str_1 = ""
    input_1 = list(input())
    for _ in range(input_1):
        input_2 = input_1
        str_1 = input_2
        print(str_1)

if __name__ == '__main__':
    main()
