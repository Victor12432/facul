# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, devo primeiramente armazenar a tabela dada no enunciado como um dicionário, assim consigo rapidamente 
descobrir a duração de cada nota. Uma vez que sei isso, basta acumular o valor de cada nota num mesmo compasso.
Note que na leitura posso utilizar diretamente o input().split('/') para quebrar os compassos pelo /
Após isso, basta percorrer cada compasso acumulando a soma das notas. Por fim, ao terminar de percorrer um compasso
verifico se a soma das notas dele é igual à 1. Devo apenas cuidar para comprar números com ponto decimal, assim 
a solução é verificar se a diferença de 1 e a soma das notas é menor que um certo decimal muito pequeno.
'''

duracao = {}
duracao['W'] = 1
duracao['H'] = 1/2.0
duracao['Q'] = 1/4.0
duracao['E'] = 1/8.0
duracao['S'] = 1/16.0
duracao['T'] = 1/32.0
duracao['X'] = 1/64.0

while True:
    compassos = input().split('/') #Descubro todos os compassos
    if compassos[0] == '*':
        break
    
    qtde = 0 #Acumulo a quantidade de compassos cuja soma das notas é igual à 1
    for c in compassos: # Para cada compasso, inicio a soma de suas notas com 0 
        soma = 0
        for i in range(len(c)): #Acumulo a duração de cada nota do compasso c
            soma += duracao[c[i]]
        
        if abs(soma - 1.0) < 0.000000001: #Se a soma for igual à 1, então incremento a quantidade de compassos cuja soma das notas é 1
            qtde += 1
    
    print(qtde)