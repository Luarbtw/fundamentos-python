from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto ou não (digite 0 para verificar o ano atual): '))
bis = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if ano == 0:
    ano = date.today().year
if bis:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')