n = int(input("Digite um numero: "))
resposta = str(input("Quer continuar? [S/N] ")).lower()
contador = 1
soma = n
maior = menor = n 

while resposta == "s":
    n = int(input("Digite um numero: "))
    resposta = str(input("Quer continuar? [S/N] ")).lower()
    soma += n
    
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    
    contador += 1

print(f"Você digitou {contador} numeros e a media foi {soma/contador}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
    


    
    