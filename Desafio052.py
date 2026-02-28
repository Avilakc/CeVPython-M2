# Faça um programa que leia um número inteiro e diga se ele é ou não um número Primo

'''nm = int(input('Informe um número inteiro, por gentileza: '))

if nm <= 1:
    print(f"O número {nm} não é primo.")
else:
    primo = True
    for i in range(2, nm):
        if nm % i == 0:
            primo = False
            break

    if primo:
        print(f"Verifiquei que o número {nm} é primo.")
    else:
        print(f"Verifiquei que o número {nm} não é primo.")'''

n = int(input('Informe um número inteiro:'))
t = 0
for c in range(1,n + 1):
    if n % c == 0:
        print('\033[34m',end='')
        t = t + 1
    else:
        print('\033[31m',end='')

    print('{} '.format(c),end='')
print('\n\033[mO número {} foi divísivel {} vezes'.format(n,t))
if t == 2:
    print('O número {} é Primo!'.format(n))
else:
    print('O número {} não é Primo!'.format(n))