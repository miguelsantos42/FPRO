def shopping(alist, stock):
    count = 0
    missing = {}

    for item, quant_desejada in alist.items:
        if item in stock:
            quantidade_stock, preco = stock[preco]
            quantidade_comprada = min(quant_desejada, quantidade_stock)
            count += quantidade_comprada * preco
        
            if quant_desejada > quantidade_stock:
                missing[item] = quant_desejada - quantidade_stock
        
        else:
            missing[item] = quant_desejada
    
    return count, missing

print((shopping({'banana': 10, 'maçãs': 20, 'laranjas': 30}, {'banana': (30, 3), 'maçãs': (10, 2)})))
print((shopping({'banana': 10, 'maçãs': 20, 'laranjas': 30}, {'banana': (10, 3), 'maçãs': (20, 2), 'laranjas' : (30, 1)})))






