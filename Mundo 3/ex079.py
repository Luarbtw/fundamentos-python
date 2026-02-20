lista = []

while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
    else: 
        print("Valor duplicado")

    resposta = str(input("Deseja continuar? [S/N] "))
    if resposta in 'Ss':
        continue
    elif resposta in 'Nn':
        break

print(lista.sort())