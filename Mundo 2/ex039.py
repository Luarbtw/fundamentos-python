from datetime import date

nasc = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade == 18:
    print(f'Você nasceu em {nasc} e tem {idade} anos, deve se alistar em {atual}.')
elif idade > 18:
    print(f'Você nasceu em {nasc} e tem {idade} anos, seu alistamento foi em {nasc + 18}.')
else:
    print(f'Você nasceu em {nasc} e tem {idade}anos, você deverá se alistar em {18 - idade} ano(s).')