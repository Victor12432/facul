# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema devo encontrar o primeiro elemento de uma ordenação com base em alguns critérios. Como não preciso saber quem é o segundo, terceiro, etc... apenas devo
pensar em armazenar o "primeiro atual" e sempre comparar com os seguintes verificando se alguém é melhor que ele. Para isso, posso armazenar inicialmente o primeiro
ser como o melhor de todos. Depois, para cada novo ser que eu leio, basta comparar com o ser armazenado como melhor de todos. Se o novo ser é melhor, então troco,
caso contrário mantenho o melhor. Note que não é necessário ordenar todos os seres, pois basta controlar o primeiro colocado.
'''
n = int(input())

#Inicio marcando o primeiro ser como godofor
godoforS, godoforP, godoforK, godoforM =  input().split()
godoforP = int(godoforP)
godoforK = int(godoforK)
godoforM = int(godoforM)

#Para os demais seres, comparo com o godofor atual se o novo ser é melhor ou não
for _ in range(1,n):
    s, p, k, m = input().split() #Leio o ser atual
    p = int(p)
    k = int(k)
    m = int(m)

    troca = False
    if p > godoforP: #Se o nível de poder do ser atual é maior que o do godofor atual, troco 
        troca = True
    elif p == godoforP: #Senão, se o poder for igual
        if k > godoforK: #Mas, a quantidade de deuses que o ser atual matou é maior que o do godofor atual, troco
            troca = True
        elif k == godoforK: #Senão, se a quantidade for a mesma
            if m < godoforM: #Mas, a quantidade de vezes que ser atual for menor que a do godofor atual, troco
                troca = True
            elif m == godoforM and s < godoforS: #Por fim, se tudo for igual, mas o nome do ser atual vem antes do nome do godofor atual, troco também. Note que aqui é necessário considerar a diferença entre maiúsculas e minúsculas.
                troca = True
    
    if troca: #Se o troca for True, então significa que o ser atual é melhor que o godofor atual... então troco
        godoforK = k
        godoforM = m
        godoforP = p
        godoforS = s
        
print(godoforS)