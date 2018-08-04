'''
Given a  number int_input, find the product of all the digits
example:input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
N_N = int(input())
I_I = 0
F_F = 1
for I_I in range(4):
    S_S = N_N % 10
    F_F = F_F * S_S
print(F_F)

if __name__ == "__main__":
    main()
