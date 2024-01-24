def is_palindrome(s):
    for i in range(0, len(s)//2):
        if(s[i] != s[len(s)-i-1]):
            return False
    return True

def palindrome_index(s):
    if is_palindrome(s):
        return -1
    else:
        n = len(s)
        for i in range(0, n):
            if(is_palindrome(s[:i] + s[i+1:])):
                return i
    return -1


print(palindrome_index('avjfkhjfdbkjgdfg'))
print(palindrome_index('aaab'))
print(palindrome_index('tattarrattat'))
print(palindrome_index('acbddba'))
print(palindrome_index('abba'))
print(palindrome_index('abba'))