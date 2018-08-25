'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    no_of_lines = input().split(" ")
    lines = ""
    for i in range(no_of_lines):
        lines += input() + "\n"
    print(lines)

if __name__ == '__main__':
    main()
