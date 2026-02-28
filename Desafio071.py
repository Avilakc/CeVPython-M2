'''Crie um programa que siomule op funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário quanto será o valor a ser sacado(int) e 
o programa vai informar quantas cédulas de cada valor serão entregues
Considere que o caixa possui cedulas de 50,20,10 e 1 Real.'''

print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)
v = int(input('Informe o valor a ser sacado: R$ '))
tot = v
c = 50
tc = 0
while True:
    if tot >= c:
        tot-=c
        tc+=1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de {c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if tot == 0:
            break
print('='*30)
print('VOLTE SEMPRE!')