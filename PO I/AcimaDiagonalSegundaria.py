o = input()
mat = [None] * 12 
for i in range(12):
    mat[i] = [None] * 12

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())

soma = 0
qtde = 0

# Somar os elementos acima da diagonal secundária
for i in range(12):
    for j in range(12 - i - 1):
        soma += mat[i][j]
        qtde += 1

if o == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma / qtde))