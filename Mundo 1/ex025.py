nome = str(input('Digite um nome: ')).strip().lower().split()
silva = ('silva' in nome)
if silva == True:
    print ('Esse nome tem Silva')
else:
    print ('Não tem Silva')
