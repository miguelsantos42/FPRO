def replace_rec(old_ch, new_ch, astring):
    if len(astring) == 0:
        return astring
    elif astring[0] == old_ch:
        return new_ch + replace_rec(old_ch, new_ch, astring[1:])
    else:
        return  astring[0] + replace_rec(old_ch, new_ch, astring[1:])
    

print(replace_rec("e", "_", "these are the best days"))
print(replace_rec(",", ".", "1,2,3,4,5,6,7,8,9"))
print(replace_rec("M", "#", "NY^T&^MM#M%f*zv#u"))
print(replace_rec("s", "@", "CaseSensitiveTest"))
