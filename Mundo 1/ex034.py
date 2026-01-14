s = float(input('Digite o salário do funcionário: '))
sup = s * 1.10
inf = s * 1.15
if s >= 1250.00:
    print(f'O aumento será de 10%, indo de R${s} para R${sup:.2f}')
else: 
    print(f'O aumento será de 15%, indo de R${s} para R${inf:.2f}')