def first(word, i):
    if len(word) == i:
        return ""
    else:
        letras = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
        c = word[i]
        for j in letras:
            if j == c:
                return c
        i+=1
        return first(word,i)
 

word="geeksforGeekS"
print(first(word,0))