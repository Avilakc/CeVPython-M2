# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

s = 0
ct = 0
for c in range(6):
    nm = int(input('Informe um Valor: '))
    if nm % 2 == 0:
        s += nm # s = s + nm
        ct += 1

print('A soma dos {} números pares foi de {}'.format(ct, s))