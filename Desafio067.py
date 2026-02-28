''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
'''
'''while True:
    n = int(input('Você deseja ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
print('FIM')'''

while True:
   
    v = int(input('Você deseja ver a tabuada de qual número? '))
    if v < 0:
        break
    print(f'''{v} X {1} = {v*1}
{v} X {2} = {v*2}
{v} X {3} = {v*3}
{v} X {4} = {v*4}
{v} X {5} = {v*5}
{v} X {6} = {v*6}
{v} X {7} = {v*7}
{v} X {8} = {v*8}
{v} X {9} = {v*9}
{v} X {10} = {v*10}''')
    if v < 0:
        break
print('FIM')