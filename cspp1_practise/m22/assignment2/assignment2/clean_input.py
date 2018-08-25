'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    for char in string:
        if char in "!@#$%^&*()":
            string.remove(char)
    return string
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
