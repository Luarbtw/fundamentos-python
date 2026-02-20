times = ('Bragantino', 'Palmeiras', 'Chapecoense', 'Mirassol', 'Fluminense',
        'Bahia', 'São Paulo', 'Botafogo', 'Grêmio', 'Athletico-PR')

print("=-="*30)

print(f"Os 10 primeiros times do Brasileirão são: {times}")
print("=-="*30)

print(f"Os 5 primeiros são: {times[0:6]}")
print("=-="*30)

print(f"Os 4 últimos são: {times[6:11]}")
print("=-="*30)

print(f"Os times em ordem alfabética são: {sorted(times)}")
print("=-="*30)

print(f"O chapecoense está na {times.index('Chapecoense') + 1}a posição.")
print("=-="*30)