soma = 0
contador = 0
for n in range(3, 501, 3): 
     if n % 2 != 0:       
         soma += n 
         contador += 1
print(f'Existem {contador} números múltiplos de 3 entre 1 e 500 \nA soma desses números é igual a {soma}')
