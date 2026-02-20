lista = []

while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    resposta = str(input("Deseja continuar? [S/N] "))
    if resposta in "Ss":
        continue
    elif resposta in "Nn":
        break

pares = [x for x in lista if x % 2 == 0]
impares = [x for x in lista if x % 2 != 0]

print(lista)
print(pares)
print(impares)
