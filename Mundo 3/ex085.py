lista = [[],[]]

for i in range(7):
    x = int(input(f"Digite o {i+1}o valor: "))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)


print(f"Os valores pares são: {sorted(lista[0])}")
print(f"Os valores impares são: {sorted(lista[1])}")
