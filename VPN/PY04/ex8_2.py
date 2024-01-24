def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def caesar(message):
    string = ""
    count = 0
    for i in message:
        print(ord(i) - fibonacci(count), fibonacci(count),i, ord(i))
        if 'A' <= i <= 'Z':
            if ord('A') <= (ord(i) - fibonacci(count)) <= ord('Z'):
                string += chr(ord(i) - fibonacci(count))
            else:
                string += chr(ord('A') + (-ord('A') + ord(i) - fibonacci(count)) % (ord('Z')- ord('A') + 1))
        else:
            string += i

        count += 1
    
    return string