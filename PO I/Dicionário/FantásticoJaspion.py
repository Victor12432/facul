# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, devo considera utilizar um dicionário para armazenar as traduções das palavras de japonês para português. 
Esse dicionário deve ser utilizado zerado para cada instância da entrada. Depois de preencher o dicionário com a entrada,
devo ler o texto e para cada palavra do texto pesquisar se a palavra existe ou não no dicionário. Se não existir, imprimo ela,
senão se existir, então imprimo a sua tradução. Também devo cuidar ao imprimir a primeira palavra da saída, visto que não devem haver 
espaços em branco no início e fim de cada linha.
'''
t = int(input())
for _ in range(t):
    m,n = input().split()
    m = int(m)
    n = int(n)
    
    dicio = {} #Crio meu dicionário vazio
    for i in range(m):
        a = input().strip() #Leio a palavra em japonês
        b = input().strip() #Leio a palavra em português
        dicio[a] = b #Guardo a tradução de japonẽs para português no dicionário
        
    for i in range(n): #Para cada linha do texto a ser traduzido...
        texto = input().split() #Leio a linha quebrando por palavras
        
        primeiro = True
        for k in range(len(texto)): #Para cada palavra do texto...
            if not texto[k] in dicio: #Se ela não estiver no dicionário, apenas imprimo a própria palavra. Note que texto[k] é a k-ésima palavra do texto
                if primeiro: #Uso esse primeiro para controlar se é a primeira palavra a ser impressa
                    print(texto[k], end='')
                    primeiro = False
                else:
                    print(" " + texto[k], end='')
        
            else: #Senão, se a palavra estiver no dicionário, então imprimo a sua tradução
                if primeiro:
                    print(dicio[texto[k]], end='')
                    primeiro = False
                else:
                    print(" " + dicio[texto[k]], end='')
        print()
    print()