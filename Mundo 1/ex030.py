n = int(input('Digite um número: '))
par = n % 2 == 0
impar = n % 2 != 0
if par:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar')
