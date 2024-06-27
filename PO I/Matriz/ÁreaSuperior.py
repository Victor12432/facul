o = input()
mat = [None] * 12 
for i in range(12):
    mat[i] = [None] * 12

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())

soma = 0
qtde = 0

for i in range(6):
    for j in range(1+i,11-i):
            soma += mat[i][j]
            qtde += 1

if o == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma / qtde))