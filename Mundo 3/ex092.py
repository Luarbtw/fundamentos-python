from datetime import date

ano_atual = date.today().year

pessoa = {}

pessoa['nome'] = str(input("Nome: "))
pessoa['ano_nascimento'] = int(input("Ano de Nascimento: "))
idade = ano_atual - pessoa['ano_nascimento']
pessoa['idade'] = idade
pessoa['carteira'] = int(input("Número da carteira de trabalho (0 se não tem ainda): "))

if pessoa['carteira'] != 0:
    pessoa['ano_contratacao'] = int(input("Ano de contratação: "))
    pessoa['salario'] = int(input("Salário: R$")) 
    pessoa['aposentadoria'] = idade + 35

print("-="*30)

for key, value in pessoa.items():
    print(f"{key} tem o valor {value}")
    

