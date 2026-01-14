from colorama import *

casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos para pagar tudo? '))

mensalidade = casa / (anos * 12) 

print(f'Para finaciar uma casa no valor de R${casa:.2f} em {anos} anos, a prestação será de R${mensalidade:.2f}')

if mensalidade > salário * 0.30:
    print(f'Empréstimo {Fore.RED}NEGADO{Style.RESET_ALL}')
else:
    print(f'Empréstimo {Fore.GREEN}APROVADO{Style.RESET_ALL}')
