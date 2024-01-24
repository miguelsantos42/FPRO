def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def caesar(message):
    def shift_letter(letter, shift):
        if 'A' <= letter <= 'Z':
            shifted = chr(((ord(letter) - ord('A') - shift) % 26) + ord('A'))
            return shifted
        elif 'a' <= letter <= 'z':
            shifted = chr(((ord(letter) - ord('a') - shift) % 26) + ord('a'))
            return shifted
        return letter

    fib_sequence = list(fibonacci(len(message)))
    ciphered_message = ''.join(shift_letter(letter, shift) for letter, shift in zip(message, fib_sequence))
    return ciphered_message