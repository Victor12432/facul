n = int(input())
b = [None]*n
a =[]
for i in range(0, n):
    a.append(int(input()))
for j in range(0, n):
    if a[j] == 0 and j == 0 and n == 1 or a[j] == 1 and j == 0 and n == 1:
        b[j] = a[j]
    elif a[j] == 0 and j == 0 or a[j] == 1 and j == 0:
        b[j] = a[j] + a[j+1]
    elif a[j] == 0 and j < n-1:
        b[j] = a[j+1] + a[j-1]
    elif a[j] == 1:
        if j < n-1 and a[j-1] == 0:
            b[j] = a[j] + a[j+1]
        elif j < n-1 and a[j-1] == 1:
            b[j] = a[j] + a[j+1] + a[j-1]
        else:
            b[j] = a[j-1] + a[j]
    else:
        b[j] = a[j-1] + a[j]
    print(b[j])
