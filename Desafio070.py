'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
 no final, mostre: 
 A) Qual é o total gasto na compra. 
 B) Quantos produtos custam mais de 1000 Reais. 
 C) Qual é o nome do produto mais barato.'''


b = v1 = s = c = 0
mp = ''

while True:
    c += 1
    n = str(input('Informe o nome do produto: ')).strip()
    p = float(input('Informe o preço do produto: R$'))
    s += p

    if p >= 1000:
        v1 += 1

    if  p < b or c == 1:
        b = p
        mp = n

    cond = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break

print(f'O total gasto na compra foi de R$ {s}, '
      f'{v1} produtos custaram mais de R$ 1000, '
      f'o nome do produto mais barato é {mp}')