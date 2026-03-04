from random import randint

dados = {}

print("Valores Sorteados:")

for i in range(4):
    dados[f'jogador {i+1}'] = randint(1, 6)

for key, value in dados.items():
    print(f"{key} tirou {value} no dado.")

print("-="*20)
print("Ranking dos jogadores")

for posicao, jogador in enumerate(sorted(dados, key=dados.get, reverse=True)):
    print(f"{posicao+1}o lugar: {jogador} com valor {dados[jogador]}")
