def is_prime(n):
    if n <= 1:
        return False
    if n > 1 and n <= 3:
        return True
    for j in range(2, int(n/2)+1):
        if n % j == 0:
            return False
    return True 

min = int(input())
max = int(input())

print(f"Prime numbers between {min} and {max} are: ", end="")

string = ''

for i in range(min, max+1):
    if is_prime(i):
        string+=str(i) + ' '

print(string.strip())
