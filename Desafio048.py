# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

s = 0
ct = 0
for c in range(1, 501 , 2):
  if c % 3 ==0:
     ct += 1
     s += c
print('O somátorio de todos os {} números impares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500 foi de {}'.format(ct,s))