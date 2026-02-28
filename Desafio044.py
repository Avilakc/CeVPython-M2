# Elabore um programa que calcule o valor a ser pago por um produto. Considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2k no cartão: preço normal
# em 3x ou mais no cartão: 20% de juros

# P1 - (P1 * 5 /100)
p = float(input('Informe o valor do produto que deseja comprar: R$ '))

print('Para realizar o pagamento à vista no Dinheiro/Cheque com 10% de desconto, Digite 1')
print('Para realizar o pagamento à vista no Cartão com 5% de desconto, Digite 2')
print('Para realizar o pagamento no Cartão em até 2x no Cartão, Digite 3')
print('Para realizar o pagamento no Cartão em 3x ou mais com 20% de juros, Digite 4')

op = int(input('Selecione o método de pagamento, por gentileza. (1-4): '))

if op == 1:
    print('Certo! O valor final do produto é R$ {}'.format(p - (p*10/100)))
elif op == 2:
    print('Certo! O valor final do produto é R$ {}'.format(p - (p*5/100)))
elif op == 3:
    print('Certo! O valor final do produto é R$ {}'.format(p))

elif op == 4:
   pa = int(input('Certo! Deseja parcelar em quantas vezes no cartão? '))
   if pa < 3:
       print('Valor invalido! O valor minimo de parcelas deve ser 3.')
   elif pa >= 3:
        print('Certo! O valor final do produto é R$ {}'.format(p + (p*20/100)))
else:
    print('Opção Invalida!')