def xmiddle_square(number, digits, iterations):
    result = number
    for _ in range(iterations):
        # Elevar o número ao quadrado e convertê-lo em uma string
        square_str = str(result * result)

        # Garantir que a string do quadrado tenha pelo menos 2*dígitos caracteres
        square_str = square_str.zfill(2 * digits)

        # Extrair os dígitos do meio
        middle_start = (len(square_str) - digits) // 2
        middle_end = middle_start + digits
        middle_digits = square_str[middle_start:middle_end]

        # Atualizar o resultado para a próxima iteração
        result = int(middle_digits)

    return result

print(xmiddle_square(1111, 4, 1))
print(xmiddle_square(1111, 4, 2))
print(xmiddle_square(1234, 4, 25))
print(xmiddle_square(123456, 10, 25))
