from random import randint

tupla = (randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print("Os números sorteados são:", *tupla)
print(f"O maior valor é {max(tupla)}")
print(f"O menor valor é {min(tupla)}")