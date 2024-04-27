nota = int(input())
'''
Iniciamos com a variavel nota e comparamos com os números de 0 a 100,
atribuindo uma nota de A a E para cada intervalo informado
'''
if nota >= 86 and nota <= 100:
print("A")
elif nota >= 61 and nota <= 85:
print("B")
elif nota >= 36 and nota <=60:
print("C")
elif nota >= 1 and nota <= 35:
print("D")
else:
print("E")
