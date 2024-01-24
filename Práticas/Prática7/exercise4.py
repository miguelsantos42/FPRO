def isomorphic(astring1, astring2):

    dici = {}

    for i in range(0 ,len(astring1)):
        if(astring1[i]) not in dici.keys() and astring2[i] not in dici.values():  #no caso de não estarem no dici
            dici[astring1[i]] = astring2[i]
        elif(astring1[i] in dici.keys()):
            if(astring2[i] not in dici.values()):
                return(f"'{astring1}' and '{astring2}' are not isomorphic")
        elif(astring1[i] not in dici.keys()):
            if(astring2[i] in dici.values()):
                return(f"'{astring1}' and '{astring2}' are not isomorphic")
    
    return(f"'{astring1}' and '{astring2}' are isomorphic")

print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))


