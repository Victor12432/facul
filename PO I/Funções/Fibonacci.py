def iccanobif(n):
    lista = [1, 1]
    for i in range(n):
        if n == len(lista):
            break
        soma = lista[i]+lista[i+1]
        lista.append(soma)
    lista.sort(reverse = True)
    print(' '.join(map(str, lista)))
n = int(input())

if n != 1:
   iccanobif(n)
else:
    print('1')