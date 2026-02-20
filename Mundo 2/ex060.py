numero = int(input("digite um numero: "))
contador = numero
fatorial = 1

print(f'O fatorial de {numero} é: ')

while contador > 0:
    print(contador, end = '')
    print(' x ' if contador > 1 else ' = ', end = '')
    fatorial = fatorial * contador
    contador -= 1
print(fatorial)
   



