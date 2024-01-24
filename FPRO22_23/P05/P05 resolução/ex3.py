def mask_data(data, n_characters, position):
    new_string = ""
    
    if position == "begin":
        new_string = new_string + "*" * n_characters
        for i in range(n_characters, len(data)):
            new_string = new_string + data[i]
    
    else:
        for j in range(0, len(data)-n_characters):
            new_string = new_string + data[j]
        new_string = new_string + "*"*n_characters
    
    return new_string


print(mask_data("764987002", 4, "begin"))
print(mask_data("John Wick", 0, "begin"))
print(mask_data("202101298", 5, "end"))
print(mask_data("910432409", 4, "end"))
