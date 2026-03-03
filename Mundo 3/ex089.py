alunos = []

def adicionar_lista(lista, a, b, c):
    lista.append(a)
    lista.append(b)
    lista.append(c)
    
while True:
    aluno = []
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    adicionar_lista(aluno, nome, nota1, nota2)
    alunos.append(aluno[:])
    
    resposta = str(input("Quer continuar [S/N]: "))
    if resposta in "Nn":
        break

print("-="*15)
print(f"{'Num.':<4} {'Nome':<4}{'Média':>8}")
print("--"*15)
for index, pessoa in enumerate(alunos):
    print(f"{index:<4} {pessoa[0]:<4}{(pessoa[1] + pessoa[2]) / 2:>8}")
print("--"*15)

while True:
    num_aluno = int(input("Deseja ver a nota de qual aluno? [Digite 999 pra sair]: "))
    
    if num_aluno == 999:
        print("Finalizando...")
        break

    print(f"Notas de {alunos[num_aluno][0]}: {alunos[num_aluno][1]} e {alunos[num_aluno][2]} ")
    print("--"*15)





