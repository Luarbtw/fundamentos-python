from time import sleep

operador_while = 0

while operador_while == 0:
    print("-="*20)
    valor1 = int(input("Primeiro valor: "))
    valor2 = int(input("Segundo valor: "))

    print("-="*20)
    print("[ 1 ] Somar\n[ 2 ] Subtrair\n[ 3 ] Multiplicar\n[ 4 ] Novos valores\n[ 5 ] Sair do programa")

    operacao = int(input("->>> Qual a sua opção? "))

    if operacao == 1:
        resultado = valor1 + valor2
        print(f"O resultado da operação é {resultado}.")

    elif operacao == 2:
        resultado = valor1 - valor2
        print(f"O resultado da operação é {resultado}.")

    elif operacao == 3:
        resultado = valor1 * valor2
        print(f"O resultado da operação é {resultado}.")

    elif operacao == 4:
        print("Digite novamente os valores")
        
    elif operacao == 5:
        operador_while = 1
        print("FINALIZANDO PROGRAMA...")
        sleep(1)

    else:
        print("Digite um comando válido!")

    sleep(1)