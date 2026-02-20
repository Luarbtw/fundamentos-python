tupla = ("Abacate", "Banana", "Python", "Programador")

for i in range(0, len(tupla)):
    print(f"A palavra {tupla[i]}")

    for letra in tupla[i]:
        if letra.lower() in "aeiou":
            print(f" tem {letra}")
