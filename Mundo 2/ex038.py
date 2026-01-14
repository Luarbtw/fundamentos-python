from colorama import *
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
blue = Fore.BLUE
yel = Fore.YELLOW
r = Style.RESET_ALL
if n1 > n2:
    print(f'{n1} é {blue}MAIOR{r} que {n2}')
elif n2 > n1:
    print(f'{n2} é {blue}MAIOR{r} que {n1}')
else:
    print(f'{n1} e {n2} são {yel}IGUAIS{r}')
