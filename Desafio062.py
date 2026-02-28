'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos.'''

pt = int(input('Informe o Primeiro Termo: '))
r = int(input('Informe a razão: '))
c = 1
total = 0
v = 10
while v != 0:
    total += v
    while c <= total:
        print(pt)
        pt += r
        c += 1
    print('Pausa')
    v = int(input('Quantos termos você quer mostrar a mais? '))
print('Contagem Concluida com {} Termos mostrados!'.format(total))