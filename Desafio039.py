# Faça um um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo para se alistar.

id = int(input('Quantos anos você tem? '))

if id == 18:
    print('Está na hora de se alistar!')
elif id < 18:
    print('Verifiquei que falta {} Anos para você se alistar!'.format(18 - id))
else:
   print('Verifiquei que já se passaram {} Anos do tempo correto de se alistar!'.format(id - 18))