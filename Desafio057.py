
# Faça um programa que leia o sexo de uma pessoa. Mas só aceite os valores 'M' ou 'F'. 
# #Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF' :
    sexo = str(input('Dados invalidos! Informe o seu sexo, por gentileza:')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))