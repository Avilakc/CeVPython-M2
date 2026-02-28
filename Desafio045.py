# Crie um programa que faça o computador jogar Jokenpô

from random import randint

l1 = ('Pedra', 'Papel', 'Tesoura')
game = randint(0,2)

jg = int(input('Selecione a sua jogada: \n [0] Pedra\n [1] Papel \n [2] Tesoura \n Qual é a sua jogada? '))

print('=' * 30, '\n O Computador escolheu {} \n O Jogador escolheu {}'.format(l1[game], l1[jg]))
print('=' * 30)

if jg == game:
    print('Empate!')

elif jg == 0 and game == 1 or jg == 1 and game == 2 or jg == 2 and game == 0:
    print('O Computador venceu!')

elif jg == 0 and game == 2 or jg == 1 and game ==0 or jg == 2 and game == 1:
    print('O Jogador venceu!')