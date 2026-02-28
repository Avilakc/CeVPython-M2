'''melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 a 10. Só que agora o jogador vai tentar advinhar
até acertar, mostrando no final quantos palpiites foram necessários para vencer'''


from random import randint
c = randint(0,10)
print('Pensei em um número entre 0 e 10!')
print('Você consegue advinhar em qual número pensei?')
p = 0
resposta = False
while not resposta:
    player = int(input('Qual é o seu palpite? '))
    p += 1
    if player == c:
        resposta = True
    else:
        if player < c:
            print('O número em que pensei é Maior! Tente novamente.')
        elif player > c:
            print('O número em que pensei é Menor! Tente novamente.')
print('Parábens! Você acertou com {} tentativas!'.format(p))