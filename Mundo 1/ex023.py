n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'A unidade de milhar deste número é: {m}' ) 
print(f'A centena deste número é: {c}' )
print(f'A dezena deste número é: {d}')
print(f'A unidade deste número é: {u}')

 