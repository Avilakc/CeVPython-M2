'''Faça um programa que leia um número qualquer o mostre o seu fatorial.
Realize o programa em While e em For'''

v = int(input('Você deseja descobrir o fatorial de qual número? '))
c = v
f = 1
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f)

'''v = int(input("Digite um número: "))
f = 1

for i in range(1, v + 1):
    f *= i  
print('O fatorial de {} é {}'.format(v,f))'''