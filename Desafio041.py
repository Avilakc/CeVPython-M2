# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20: Sênior
# Acima de 20: Master

id = int(input('Informe a sua idade: '))

if id <= 9:
    print('A sua idade se enquadra na categoria Mirim.')
elif id >= 10 and id <= 14:
    print('A sua idade se enquadra na categoria Infantil.')
elif id >= 15 and id <= 19:
    print('A sua idade se enquadra na categoria Junior.')
elif id ==20:
    print('A sua idade se enquadra na categoria Senior')
else:
    print('A sua idade se enquadra na categoria Master')