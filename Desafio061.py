''' refaça o Desafio 51, utilizando a estrutura de repetição While'''
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('Informe o Primeiro Termo: '))
r = int(input('Informe a razão: '))
c = 1
while c <= 10:
    print(pt)
    pt += r
    c += 1
print('Contagem Concluida!')