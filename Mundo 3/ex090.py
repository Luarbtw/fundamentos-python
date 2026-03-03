aluno = {}

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

print(aluno['nome'])
print(aluno['media'])
if aluno['media'] >= 7:
    print("Aprovado")
else:
    print("Reprovado")
