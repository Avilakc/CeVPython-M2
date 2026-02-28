# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# media abaixo de 5: Reprovado
# Media entre 5.0 e 6.9: Recuperação
# Média de 7.0 ou acima: Aprovado

n1 = float(input('Informe a sua primeira nota de 0.0 a 10.0:  '))
n2 = float(input('Informe a sua segunda nota de 0.0 a 10.0: '))
media = (n1 + n2)/2

if media < 5.0:
    print('Infelizmente você foi reprovado pois sua media de {} ficou abaixo de 5.0.'.format(media))
elif media >= 5.0 and media < 6.9:
    print('Infelizmente você ficou de recuperação, sua media foi de {}.'.format(media))
else:
    print('Muito bem! Você foi Aprovado com uma media de {}.'.format(media))