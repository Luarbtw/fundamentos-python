soma = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma de todos os valores é: {soma}')