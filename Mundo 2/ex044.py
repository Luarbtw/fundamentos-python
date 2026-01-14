print(f'{"LOJINHO":=^30}')
val = float(input('Digite o valor das compras: '))
print('FORMAS DE PAGAMENTO \n[ 1 ] à vista dinheiro/cheque \n[ 2 ] à vista no cartão \n[ 3 ] 2x o cartão \n[ 4 ] 3x ou mais o cartão')
r = int(input('Digite qual a opção de pagamento: '))

if r == 1:
    val = val - val * 0.1
    print(f'O valor total com 10% de desconto será de: R${val}')
elif r == 2:
    val = val - val * 0.05
    print(f'O valor total com 5% de desconto será de: R${val}')
elif r == 3:
    valparc = val / 2
    print(f'O valor total será de: R${val}, dividio em 2 parcelas de R${valparc:.2f}')
elif r == 4:
    val = val + (val * 0.2)
    parc = int(input('Digite o número de parcelas: '))
    valparc = val / parc
    print(f'O valor total será de R${val}, dividido em {parc} parcelas de R${valparc:.2f} ')
else:
    print('Por favor, digite apenas alguma das opções acima')
