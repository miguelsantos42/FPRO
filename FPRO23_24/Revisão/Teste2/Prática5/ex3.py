def mask_data(data, n_characters, positions):
    new_str = ""

    if positions == "begin":
        new_str += '*'*n_characters
        for i in range(n_characters, len(data)):
            new_str += data[i]


    elif positions == "end":
        for i in range(0, len(data) - n_characters):
            new_str += data[i]
        new_str += "*" * n_characters

    return new_str


print(mask_data("764987002", 4, "begin"))
print(mask_data("John Wick", 0, "begin"))
print(mask_data("202101298", 5, "end"))
print(mask_data("910432409", 4, "end"))
