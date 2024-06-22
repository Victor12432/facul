while True:
    a = str(input())
    if a[0] == '*':
        break
    else:
        a = a.split()
        b = ''
        c = ['']*len(a)
        for i in range(len(a)):
            b = a[i]
            b = (b[0]).upper()
            c[i] = b
        for j in range(len(c)):
        
            if c[j] != b:
                c[j] = 'N'
            else:
                c[j] = 'Y'
        c = "".join(c)
        if (c.count('Y')) == len(a):
            print(c[0])
        else:
            print('N')