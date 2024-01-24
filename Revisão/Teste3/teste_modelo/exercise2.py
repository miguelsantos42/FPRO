def shopping(alist, stock):
    spent = 0
    missing = {}

    for i, v in alist.items:
        if i in stock:
            quantidade, preco = stock[i]
            quant_compra = min(v, quantidade)
            spent += preco * quant_compra

            if quant_compra > quantidade:
                missing[i] = quant_compra - quantidade

        else:
            missing[i] = quant_compra
    
    return spent, missing

print((shopping({'banana': 10, 'maçãs': 20, 'laranjas': 30}, {'banana': (30, 3), 'maçãs': (10, 2)})))
print((shopping({'banana': 10, 'maçãs': 20, 'laranjas': 30}, {'banana': (10, 3), 'maçãs': (20, 2), 'laranjas' : (30, 1)})))


