# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdrecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code heretemp=0
    if a<b:
    	temp=a
    	a=b
    	b=temp
    if a % b == 0:
    	return b
    else:
        return gcdrecur(b, a%b)	
def main():
    data = input()
    data = data.split()
    print(gcdrecur(int(data[0]),int(data[1])))

if __name__== "__main__":
    main()