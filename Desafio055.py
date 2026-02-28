# Faça um programa que leia o peso de 5 pessoas e informe qual foi o Maior e o Menor peso. 
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Informe o peso da {}º Pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    
print('A pessoa mais pesada está com {}kg.'.format(maior))
print('A Pessoa mais magra está com {}kg.'.format(menor))

# Exercício realizado após assistir a correção.