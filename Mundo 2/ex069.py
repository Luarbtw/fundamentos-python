maiores = 0
homem = 0
mulher = 0

while True:
    print("-"*30)
    print("Cadastre uma pessoa")
    print("-"*30)

    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: ")).strip().upper() [0]

    if idade > 18:
        maiores += 1

    if sexo == 'M':
        homem += 1

    if idade < 20 and sexo == 'F':
        mulher += 1

    escolha = str(input("Quer continuar? [S/N]: ")).strip().upper() [0]
    if escolha == 'N':
        print('='*30)
        break

print(f"Total de pessoas com mais de 18 anos: {maiores}\nAo todo temos {homem} homens cadastrados \nE {mulher} mulheres com menos de 20 anos.")
    
