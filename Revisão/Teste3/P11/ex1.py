def merge(xs, ys):
    result = []
    i = j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1

    # Add the remaining elements from both lists, if any
    result.extend(xs[i:])
    result.extend(ys[j:])

    return result

def msort(xs):
    if(len(xs) <= 1):
        return xs
    half = len(xs)//2
    first = msort(xs[:half])
    second = msort(xs[half:])
    return merge(first, second)

print(msort([3, 2, 1, 4]))
print(msort([3, 3]))
print(msort([7, 3, 1, 2, 4, 5, 6]))
print(msort([7, 3, 1, 2, 4, 5, 6, 3, 2, 5, 6, 1]))

