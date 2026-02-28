'''crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. Desconsiderando a flag(999). UTILIZANDO O BREAK'''

n = s = c = 0

while True:
    s +=n
    n = int(input(f'Digite o {c} número: [999 PARA PARAR]: '))
    if n == 999:
        break
    c += 1
print(f'A soma dos {c} números é igual a {s}')