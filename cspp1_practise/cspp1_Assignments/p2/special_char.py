'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
AUTHOR=Viswas
date:4-8-2018
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    s_s = ''
    for i_i in str_input:
        if i_i in '!@#$%^&*':
            i_i = ""
            s_s = s_s + i_i
            print(s_s)

if __name__ == "__main__":
    main()
