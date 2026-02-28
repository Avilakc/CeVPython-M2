'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar.
 No final mostre: 
A) Quantas pesssoas tem mais de 18 anos. 
B) Quantos homens foram cadastrados 
C) Quantas mulheres tem menos de 20 anos.'''




mnm = ch= ma = c = 0
while True:
    c+=1
    print(f'{c} Cadastro:')
    sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        ma+=1
    if sexo in 'mM':
        ch+=1
    if idade < 20 and sexo in 'fF':
        mnm+=1

    cond = str(input('Deseja continuar? [S/N]'))
    if cond in 'Nn':
        break
print(f'{ma} Pessoas tem mais de 18 Anos, {ch} Homens foram cadastrados, {mnm} Mulheres possuem menos de 20 Anos.')