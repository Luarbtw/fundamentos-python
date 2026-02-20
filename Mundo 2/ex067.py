while True:
    print("="*40)
    n = int(input("Digite um valor para ver sua tabuada: "))
    print("="*40)

    if n < 0:
        print("Fim do programa.")
        break

    print(f"Essa é a tabuada de {n}:")

    for i in range (10):
        print(f"{n} x {i+1} = {n*(i+1)}")
