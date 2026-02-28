'''Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci'''

valor = int(input('Quantos termos você deseja ver? '))
t1 = 0
t2 = 1 
print('{} \n{}'.format(t1,t2))
cont = 3
while cont <= valor:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont +=1
print('FIM')