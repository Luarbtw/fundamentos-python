n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))

tupla = (n1, n2, n3, n4)
print(f"O número 9 aparece {tupla.count(9)} vezes")

if 3 in tupla: 
    print(f"O número 3 aparece na {tupla.index(3) + 1}a posição")
else:
    print("Não tem o número 3")

print("Os números pares são: ", end='')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
print('')

