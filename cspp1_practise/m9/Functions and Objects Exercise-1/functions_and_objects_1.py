'''#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]

Author: Viswas
Date:8-8-2018
'''

def apply_to_each(L, f):
    for i in range(len(L)):
        L[i]=f(L[i])
    print(L)

def main():
    data = input()
    data1 = data.split()
    list1 = []
    for j in data1:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
