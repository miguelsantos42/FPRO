le = int(input())
re = int(input())
pe = int(input())
te = int(input())

if((le < 0 or le > 100) or (re < 0 or re > 100) or (pe < 0 or pe > 100) or (te < 0 or te > 100)):
    print('Input error')

elif(pe < 40 or te < 40):
    print("RFF")

else:
    print(round((le + re + 13 * pe + 5 * te) / 100))


