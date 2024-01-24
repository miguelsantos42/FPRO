#implementação sem usar o generator function
# def get_composites(n):
#     lista = list(p for p in range(3,n+1) for i in range(2,p) if p % i == 0 )
#     return list(x for x in range(4,n+1) if x in lista)


#implementação com o generator function
def get_composites(n):
    for num in range(4, n+1):
        if any(num % i == 0 for i in range(2,num)):
            yield num



print(get_composites(4))
print(get_composites(6))
print(get_composites(7))
print(get_composites(10))