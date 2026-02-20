contador = 0
soma = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    soma += n
    contador += 1

print(f"Você digitou {contador} valores e a soma desses valores é {soma}")
