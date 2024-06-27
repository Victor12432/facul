'''
O programa recebe os ingredientes A,B e C (xícaras de farinha de trigo, ovos e colheres de sopa de leite respectivamente)
e verifica quantos bolos seria possível fazer com cada um dos elementos
após isso, o programa diz a quantidade mínima de bolos possíveis de serem feitos.
'''

A, B, C = input().split()
A,B,C = int(A), int(B), int(C)

A = A // 2
B = B // 3
C = C // 5

print(min(A,B,C))
