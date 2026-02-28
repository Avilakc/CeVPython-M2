# Escreva um programa para aprovar empréstimos bancários para a compra de uma casa.
# O Programa vai perguntar o valor da casa e o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

emp = float(input('Qual é o Valor da casa que o senhor(a) deseja comprar? : R$ '))
tim = int(input('Em quantos anos você deseja pagar o empréstimo? '))
sal = float(input('Qual é o seu salário atual? : R$ '))

per = sal * 0.30
ms = tim * 12
msemp = emp / ms

if per >= msemp:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')