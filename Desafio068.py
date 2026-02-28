'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador Perder, mostrando o total de vítorias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jog + comp
    tipo = str(input('Você deseja ser Par ou Ímpar? [P/I]')).strip().upper() [0]
    print(f'Você jogou {jog} e o computador jogou {comp}. Total de {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v+=1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
        else:
            print('Você Perdeu!')
            break
print(f'Game Over! Você venceu {v} vezes.')