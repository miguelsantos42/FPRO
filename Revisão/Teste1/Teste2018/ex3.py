i = 1
n = int(input())
names = []
ages = []

while i < n:
    name = str(input("Nome: "))
    names.append(name)
    age = int(input("Idade: "))
    ages.append(age)
    i += 1

for i in names:
    for j in ages:
        print(f"{i}-{j}", end= " ")
        break
