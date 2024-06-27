# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, note que devemos armazenar a tradução da saudação Merry Christmas nas diversas línguas de entrada. Aqui cabe
bem o uso de dicionário para isso, onde a chave do dicionário é a língua e o valor de cada chave é a saudação naquela língua.
Depois de ler todas as saudações em todas as línguas, note que basta ler os nomes das crianças e nacionalidades para simplesmente
consultar o dicionário e imprimir a saudação na nacionalidade da criança.
'''
dicio = {} #Crio um dicionário para armazenar a saudação em cada língua
n = int(input())
for _ in range(n):
    a = input() #Leio a língua
    b = input() #Leio a saudação
    dicio[a] = b #Armazeno ela no dicionário
    
m = int(input())
for _ in range(m):
    c = input() #Leio o nome da criança
    a = input() #Leio a nacionalidade
    
    print(c) #Imprimo o nome da criança
    print(dicio[a]) #Imprimo a saudação na nacionalidade da criança
    print() #Note que após cada etiqueta devo sempre imprimir uma linha em branco