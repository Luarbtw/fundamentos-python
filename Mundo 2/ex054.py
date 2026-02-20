'''Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
ano = date.today().year
maiores = 0
menores = 0
for x in range(7):
    nasc = int(input(f'Digite o ano de nascimento da {x + 1}ª pessoa: ')) 
    if ano - nasc >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Das 7 pessoas das quais você digitou o ano de nascimento, {maiores} é(são) de maior')
print(f'Das 7 pessoas das quais você digitou o ano de nascimento, {menores} é(são) de menor')