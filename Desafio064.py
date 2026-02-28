'''crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. Desconsiderando a flag(999).'''

'''n = cont = soma = 0
n = int(input('Informe um número [Digite 999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Informe um número: [Digite 999 para parar]: '))
print('Você digitou {} números e a soma entre eles é de {}'.format(cont,soma))'''

n = s = c = 0
while True:
    c +=1
    n = int(input('Digite um número: '))
    if n == 999:
        c -= 1
        break
    s+=n
print(f'A soma dos {c} números é igual a: {s}')