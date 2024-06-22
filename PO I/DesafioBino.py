n = int(input())
k = n-1
f = n+1
p = input().split() 
m = [[2],[3],[4],[5]]
for i in range(0, n):
    p[i] = int(p[i]) 
for i in range(0,4):
    m[i] = m[i]*f
for i in range(0,4):
    soma = 0
    for j in range(1,f):
        m[i][j] = p[j-1]
        if m[i][j]%m[i][0] == 0:
                soma += 1
    print('%d Multiplo(s) de %d' % (soma, m[i][0]))