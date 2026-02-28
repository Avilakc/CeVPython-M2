#Desenvolva umalógica que leia o peso ea altura de uma pessoa, calcule seu IMC e mostra seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 a 25: peso deal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

# IMC = peso em kilos / (altura * altura) em metros

print('Vamos calcular o seu IMC! Por gentiliza, responda as perguntas abaixo:')
al = float(input('Me informe a sua altura em centimetros, por gentileza: '))
ps = float(input('Me informe o seu Peso, por gentileza: '))

cnv = al/100
imc = ps / (cnv * cnv)

if imc < 18.5: 
    print('Seu IMC é de {:.2f} E você se encontra Abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25: 
    print('Seu IMC é de {:.2f} E você se encontra no Peso Ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.2f} E você se encontra com Sobre Peso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.2f} E você se encontra com Obesidade.'.format(imc))
else: 
    print('Seu IMC é de {} E você se encontra com Obesidade Mórbida'.format(imc))