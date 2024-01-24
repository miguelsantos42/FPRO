def lost_element(s1,s2):

    if len(s1) > len(s2):
        for i in s1:
            if i not in s2:
                return i
    
    else:
        for j in s2:
            if j not in s1:
                return j
            

print(lost_element({1, 4, 5, 7, 9}, {9, 4, 5, 7}))
print(lost_element({2, 3, 4, 5}, {2, 3, 4, 5, 6}))
print(lost_element(set(), {4}))
