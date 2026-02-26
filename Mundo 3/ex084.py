lista = []
mais_pesados = []
mais_leves = []

while True:
    pessoas = []
    nome = str(input("Digite o nome da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    pessoas.append(nome)
    pessoas.append(peso)

    lista.append(pessoas[:])

    resposta = str(input("Deseja continuar? [S/N] "))
    if resposta in "Ss":
        continue
    elif resposta in "Nn":
        break

maior_peso = lista[0][1]
menor_peso = lista[0][1]

for pessoa in lista:
    if pessoa[1] > maior_peso:
        mais_pesados.clear()
        mais_pesados.append(pessoa[0])
        maior_peso = pessoa[1]

    elif pessoa[1] == maior_peso:
        mais_pesados.append(pessoa[0])

    if pessoa[1] < menor_peso:
        mais_leves.clear()
        mais_leves.append(pessoa[0])
        menor_peso = pessoa[1]

    elif pessoa[1] == menor_peso:
        mais_leves.append(pessoa[0])

print(f"Você cadastrou no total {len(lista)} pessoas")
print(f"As pessoas mais leves são {mais_leves} e possuem {menor_peso}KG")
print(f"As pessoas mais pesadas são {mais_pesados} e possuem {maior_peso}KG")
print(lista)
