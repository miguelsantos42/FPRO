def C(n, r):
    if n == 0 or n == 1:
        return 1
    else: 
        total_n = 1
        total_r = 1
        total_n_r = 1

        #fatorial n
        for i in range(n, 1, -1):
            total_n = total_n * i

        #fatorial r
        for j in range(r, 1, -1):
            total_r = total_r * j

        #fatorial_n_r
        for k in range(n-r, 0, -1):
            total_n_r = total_n_r * k

        numerador = total_n
        denominador = total_r * total_n_r

        total = numerador/denominador

        return round(total)

