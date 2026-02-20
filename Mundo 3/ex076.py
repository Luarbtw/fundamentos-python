tupla = ("Lápis", "R$ 1.75", "Caderno", "R$ 2.00", "Borracha", "R$ 15.90", "Estojo", "R$ 4.20")
print('-' * 37)
print(f"{'Listagem de Preços':^40}")
print('-' * 37)
for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f"{tupla[posicao]:.<30}", end ='')
    else:
        print(tupla[posicao])
print('-' * 37)