# Crie um programa que leia o ano de nascimento de sete pessoas. E mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

an = date.today().year
tma = 0
tme = 0
for c in range(1,8):
    n = int(input('Informe o ano de nascimento da {}º pessoa: '.format(c)))
    idat = an - n
    if idat >=18:
        tma += 1
    else:
        tme += 1
print('{} Pessoas são maiores de idade.\n{} Pessoas são menores de idade.'.format(tma,tme))