from colorama import *
n = int(input('Digite um número: '))
v = Fore.GREEN
rs = Style.RESET_ALL

print(f'[ {v}1{rs} ] Digite para converter para {v}Hexadecimal{rs}\
\n[ {v}2{rs} ] Digite para converter para {v}Binário{rs}\
\n[ {v}3{rs} ] Digite para converter para {v}Octal{rs}') #ESSES \N QUEBRAM A LINHA E OS \ FAZEM A LEITURA DA STRING CONTINUAR

choice = int(input('Qual? '))

if choice == 1:
    print(hex(n).replace('0x', ''))
elif choice == 2:
    print(bin(n).replace('0b', ''))
elif choice == 3:
    print(oct(n).replace('0o', ''))
else:
    print('Por favor, digite apenas 1, 2 ou 3')
