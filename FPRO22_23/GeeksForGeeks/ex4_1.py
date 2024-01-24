def first(word, index):
    if len(word) == index:
        return ""
    else:
        if(str(word[index]).isupper()):
            return word[index]
    index+=1
    return(first, index)


print(first("geeksforGeek",0))
