while True:
    d,n = input().split()
    d,n,p= str(d),list(n),[]
    if d == '0' and n == ['0']:
        break
    while d in n:
        n.remove(d)
        p = ['0']*len(n)
    while True:
        if n == p:
            n = '0'
            break
        else:
            break
    while '0' in n:
        for i in range(len(n)):
            if n[0] == '0' and len(n) != 1:
                n.remove('0')
            else:
                break
        break
    n = "".join(n)
    print(n)