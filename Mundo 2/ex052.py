from colorama import *
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

n = int(input('Digite um número: '))

contador = 0

for c in range(1, n + 1):
    primo = n % c == 0
    if primo == True:
         print(f'{green}{c}{reset}', end = ' ')
         contador += 1
    else:
         print(f'{red}{c}{reset}', end = ' ')

print(f'\nEsse número é divisível por {contador} números. Portanto:')

if contador == 2:
    print(f'{green}É PRIMO{reset}') 
else:
    print(f'{red}NÃO É PRIMO{reset}')