# Refaça o Desafio 09, mostrando a tabuada de um número que o usuário escolher, utilizando o laço FOR.

'''n = int(input('Informe um número que deseja saber a tabuada: '))
print('A tabuada de {} é:'.format(n))
for c in range(n, n * 10 + 1, n):
    print(c)'''

n = int(input('Informe um número que deseja saber a tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n, c, n*c))