'''
o programa recebe as idades da mãe e dos dois filhos e subtrai a idade
dos dois da idade da mãe, para encontrar a idade do terceiro filho,
após isso printa a idade do mais filho por meio da função Max
'''
m = int(input())
a = int(input())
b = int(input())
c = m - (a+b)
print(max(a,b,c))
