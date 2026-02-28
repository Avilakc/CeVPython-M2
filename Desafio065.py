'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar se o usuário deseja continuar ou não a digitar valores.'''

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int (input( 'Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input( 'Quer continuar? [S/N] ')). upper(). strip( ) [0]
média = soma / quant
print( 'Vecê digitou {} números e a média foi {}'. format (quant, média))
print('0 maior valor foi {} e o menor foi {}'. format(maior, menor))