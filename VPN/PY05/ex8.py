def remove_leading(ip):
    lista = ip.split('.')
    new_string = []

    for i in lista:
        if i.isdigit():
            new_str = str(int(i))
            new_string.append(new_str)

    return '.'.join(new_string)

print(remove_leading('255.024.01.01'))
print(remove_leading('192.168.0.24'))
print(remove_leading('00.0.0000.0'))
print(remove_leading('127.56.10.100'))
