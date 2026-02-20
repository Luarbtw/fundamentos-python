from colorama import *
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
r = Style.RESET_ALL

if m < 5:
    print(f'A média é {m:.2f} e o aluno está {red}REPROVADO{r}.')
elif m > 5 and m <= 6.99:
    print(f'A média é {m:.2f} e o aluno está de {blue}RECUPERAÇÃO{r}.')
else:
    print(f'A média é {m:.2f} e o aluno está {green}APROVADO{r}.')