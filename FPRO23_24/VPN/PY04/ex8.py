from math import sqrt
#def fibonacci(n):
#    if n == 0 or n == 1:
#        return n
#    return fibonacci(n-2) + fibonacci(n-1)

def fibonacci(n):
    return round((1+sqrt(5))**n-(1-sqrt(5))**n)/((2**n)*sqrt(5))


def caesar(message):
    string = ""
    count = 0
    for i in message:
        #print(ord(i) - fibonacci(count), fibonacci(count),i, ord(i))
        if 'A' <= i <= 'Z':
            if ord('A') <= (ord(i) - int(fibonacci(count))) <= ord('Z'):
                #print(int(fibonacci(count)))
                string += chr(ord(i) - int(fibonacci(count)))
            else:
                string += chr(ord('A') + (-ord('A') + ord(i) - int(fibonacci(count))) % (ord('Z')- ord('A') + 1))
        else:
            string += i

        count += 1
    
    return string

print(caesar('HELLO WORLD!'))
print(caesar('CAESAR CIPHER'))
print(caesar('FIBONACCI SEQUENCE'))
print(caesar('SUPER IMPORTANT MESSAGE!'))
