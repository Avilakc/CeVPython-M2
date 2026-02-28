#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilatero: todos os lados iguais
#  Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

l1  = float(input('Informe o comprimento da primeira reta: ')) 
l2 = float(input('Informe o comprimento da segunda reta: '))
l3 = float(input('Informe o comprimento da terceira reta: '))

# l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    
if l1 == l2 == l3:
    print('Verifiquei que as 3 retas informadas podem formar um triângulo!')
    print('Verifiquei que este triângulo é Equilatero.')
elif l1 == l2 or l1 ==l3 or l2 == l3 and l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Verifiquei que as 3 retas informadas podem formar um triângulo!')
    print('Verifiquei que este triângulo é Isóceles.')
elif l1 != l2 or l1 !=l3 or l2 != l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Verifiquei que as 3 retas informadas podem formar um triângulo!')
    print('Verifiquei que este triângulo é Escaleno.')
else: 
    print('Verifiquei que as 3 retas informadas, não podem formar um triângulo!')