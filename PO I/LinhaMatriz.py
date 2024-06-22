n = int(input())
t = input()
mat = [None]*12
for i in range(12):
    mat[i] = [None]*12
for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())
soma = 0
qtde= 12
for i in range(12):
    soma += mat[n][i]
if t == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma/qtde))
