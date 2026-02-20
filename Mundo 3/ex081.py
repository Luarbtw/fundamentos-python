lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    resposta = str(input("Deseja continuar? [S/N] "))

    if resposta in "Ss":
        continue
    elif resposta in "Nn":
        break

print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são {sorted(lista, reverse = True)}")

print("O número 5 está na lista" if 5 in lista else "O número 5 não está na lista")  
