from math import factorial

def fatorial(i,j):
    return factorial(i)/(factorial(j)*(factorial(i-j)))

def pascal(n):
    string = ""

    for i in range(n):
        for j in range(i+1):
            string = string + str(int(fatorial(i,j))) + " " 
        string = string.strip() + '\n'

    return string

print(pascal(3))