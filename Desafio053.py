# Crie um programa que leia uma frase qualquer e informe se ela é um Palíndromo, desconsiderando os espaços.

f = str(input('Informe uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j) -1, -1, -1):
    i += j[l]
print('A frase digitada foi {}. O inverso desta frase é {}.'.format(j,i))
if i == j:
    print('Está frase é um Palíndromo!')
else:
    print('Está Frase não é um Palíndromo.')