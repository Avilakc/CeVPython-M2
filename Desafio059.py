''' Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3]  Maior
[4]  Novos números 
[5] Sair do Programa
 Seu programa deverá realizar a operação solicitada em cada caso '''

v1 = int(input('Informe o Primeiro Valor: '))
v2 = int(input('Informe o Segundo valor: '))
o = 0
while o != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior 
[4] Novos números 
[5] Sair do Programa''')
    o = int(input('Qual é a sua opção? '))
    if o == 1:
        print('O valor de {} + {} é {}'.format(v1,v2, v1 + v2))
    elif o == 2:
        print('{} x {} é igual a: {}'.format(v1,v2,v1*v2))
    elif o == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O Maior valor é {}'.format(maior))
    elif o == 4:
        print('Informe os valores novamente:')
        v1 = int(input('Informe o Primeiro Valor: '))
        v2 = int(input('Informe o Segundo Valor: '))
    elif o == 5:
        print('Programa Encerrado!')
    else:
        print('Opção invalida! Informe novamente, por gentileza: ')