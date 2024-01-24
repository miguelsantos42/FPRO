def count(phrase, letter):
    count = phrase.count(letter)
    if count != 0:
        return count
    else:
        return -1