# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, fazemos novamente uso de um dicionário. Devemos utilizar ele para armazenar cada assinatura de cada nome, ou seja,
mapear nome para assinatura.
Depois, verificamos para cada nome e assinatura escrita na folha da chamada o seguinte:
1) Percorremos toda a assinatura original e a assinatura da chamada para o nome dado na chamada. Se houver diferença em alguma posição, anotamos
2) Se a quantidade de diferenças encontradas for superior à 1, então somamos a quantidade de assinaturas falsas
'''
while True:
    n = int(input())
    if n == 0:
        break
    
    assinaturas = {} #Criamos um dicionário vazio
    for _ in range(n):
        a,b = input().split() #Lemos cada nome e assinatura original
        assinaturas[a] = b #Armazenamos o nomee a assinatura num dicionário
    
    falsas = 0    
    m = int(input())
    for _ in range(m):
        a,b = input().split() #Lemos cada nome e assinatura na chamada
        diferencas = 0 
        for i in range(len(b)): #Contamos a quantidade de diferenças entre a assinatura original e a escrita na chamada
            if assinaturas[a][i] != b[i]: #Comparamos cada posição da assinatura original com a assinatura da chamada
                diferencas += 1
        if diferencas > 1: #Se houver mais de 1 diferença, então somamos a quantidade de assinaturas falsas
            falsas +=1
            
    print(falsas)