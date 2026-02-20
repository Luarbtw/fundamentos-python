lista = []
for i in range(5):
    n = int(input(f"Digite um valor para a posição {i}: "))
    lista.append(n)

print(f"O maior valor foi {max(lista)} e aparece na posição: ", end = '')

for index, valor in enumerate(lista):
    if valor == max(lista):
        print(f"{index}... ", end = '')

print()

print(f"O menor valor foi {min(lista)} e aparece na posição: ", end = '')

for index, valor in enumerate(lista):
    if valor == min(lista):
        print(f"{index}... ", end = '')