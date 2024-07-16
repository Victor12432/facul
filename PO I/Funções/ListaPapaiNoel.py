def listaOrdenada(nome, n):
    lista = []
    somab = 0
    somam = 0
    for _ in range(n):
        name = []
        if nome.count('-') == 1:
            name = nome.split('-')
            lista.append(name[1])
            somab += 1
        else:
            name = nome.split('+')
            lista.append(name[1])
            somam += 1
    lista = sorted(lista)
    for k in lista:
        print(k)
n = int(input())
for _ in range(n):
    nome = str(input())
listaOrdenada(nome, n)