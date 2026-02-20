lista = []
pares = []
impares = []
while True:
    n = (int(input("Digite um valor: ")))
    lista.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resposta = str(input("Deseja continuar? [S/N] "))

    if resposta in "Ss":
        continue
    elif resposta in "Nn":
        break

print(f"A lista completa é: {lista}")
print(f"A lista dos pares é: {pares}")
print(f"A lista dos impares é: {impares}")