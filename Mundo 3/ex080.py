lista = []
for i in range(5):
    n = int(input("Digite um valor: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        index = 0
        while index < len(lista):
            if n < lista[index]:
                lista.insert(index, n)
                break
            index += 1    

print(f"A lista ordenada é: {lista}")