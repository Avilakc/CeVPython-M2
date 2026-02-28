# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A media de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

midade = 0
hvelho = 0
nvelho = ''
mulher20 = 0
for i in range(1,5):
    print('{}º Pessoa'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    midade += idade
    if sexo in 'Mm' and idade > hvelho:
        hvelho = idade
        nvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print('A media da idade do grupo é de {} Anos.'.format(midade / 4))
print('O nome do Homem mais velho é {} e ele tem {} Anos.'.format(nvelho,hvelho))
print('Há {} Mulheres com menos de 20 Anos.'.format(mulher20))