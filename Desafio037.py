# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 Para Binário, 2 Para Octal e 3 Para Hexadecimal.

dec = int(input('Informe um número inteiro: '))
cal = int(input('Certo! Para converter, selecione: 1 Para Binário, 2 Para Octal e 3 Para Hexadecimal: '))
if cal == 1:
    print(bin(dec))
if cal == 2:
    print(oct(dec))
if cal == 3:
    print(hex(dec))