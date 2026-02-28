# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem.
# O primeiro valor é maior que o segundo.
# # O segundo valor é maior que o primeiro.
# Não existe valor maior, os dois valores são iguais.

n1 = int(input('Informe o primeiro número inteiro: '))
n2 = int(input('Informe o segundo número inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior que o segundo')
elif n2 > n1:
    print('O segundo valor é maior que o primeiro.')
elif n1 == n2: 
    print('Não existe valor maior, os dois valores são iguais')