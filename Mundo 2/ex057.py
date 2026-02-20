sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido, digite seu sexo [M/F]: ')).upper()
if sexo == 'M' or 'F':
    print(f'Sexo {sexo} válido'.replace('F', 'FEMININO').replace('M', 'MASCULINO'))
