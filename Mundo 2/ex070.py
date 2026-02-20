total = 0
maismil = 0
preco_mais_barato = None
nome_mais_barato = None

print("LOJA TOTALMENTE REAL")

while True:
    print("-"*30)
    nome = str(input("Informe o nome do produto: "))
    preco = int(input("Informe o preço do produto: "))
    print("-"*30)

    total += preco

    if preco_mais_barato is None:
        preco_mais_barato = preco
        nome_mais_barato = nome

    elif preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome

    if preco > 1000:
        maismil += 1
    
    escolha = str(input("Quer continuar? [S/N]: ")).upper().strip() [0]
    if escolha == 'N':
        break

print(f'O total gasto foi de R${total}\n{maismil} produtos custam mais que R$1000\nO produto mais barato é "{nome_mais_barato}", que custa R${preco_mais_barato}')


