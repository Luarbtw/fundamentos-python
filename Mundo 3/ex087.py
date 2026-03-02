matriz = [[],[],[]]
soma_pares = 0
soma_coluna = 0
maior_linha = 0

for linha in range(3):
    for coluna in range(3):
        x = int(input(f"Digite um valor pra posição [{linha}, {coluna}]: "))
        if x % 2 == 0:
            soma_pares += x

        if coluna == 2:
            soma_coluna +=x

        if linha == 1 and coluna == 0:
            maior_linha = x
        elif x > maior_linha:
            maior_linha = x

        matriz[linha].append(x)

for linha in matriz:
    for num in linha:
        print(f"[{num}]", end=' ')
    print()

print(f"A soma dos numeros pares é {soma_pares}")
print(f"A soma dos numeros da terceira coluna é {soma_coluna}")
print(f"O maior valor da segunda linha é: {maior_linha}")