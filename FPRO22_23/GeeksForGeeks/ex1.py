def mycopy(s1,s2,i):
    if len(s2) == 0:
        return s1
    else:
        s2[i] = s1[i]
        i+=1
        return mycopy(s1, s2, i)
    
x = input("hello")
y = input("no")
print(mycopy(x, y, 0))