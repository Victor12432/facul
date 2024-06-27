# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, note que para encontrarmos o valor sem par basta encontrarmos uma quantidade ímpar de ocorrências de algum valor.
Para fazer a contagem de ocorrências dos valores informados, podemos usar um dicionário, onde a chave do dicionário é o valor informado. Para cada chave armazeno então a quantidade de ocorrências de cada valor. Por fim, basta percorrer todas as chaves do dicionário buscando pelo valor com quantidade de ocorrências sendo um número ímpar.
'''
while True:
    n = int(input())
    if n == 0:
        break

    ocorrencias = {} #Esse dicionário irá manter a quantidade de vezes que cada valor apareceu na entrada
    numeros = input().split()
    for i in range(n): #Para cada valor da entrada
        if not numeros[i] in ocorrencias: #Se ele ainda não aparece no dicionário, então digo que ele aparece uma vez
            ocorrencias[numeros[i]] = 1
        else: #Caso contrário, somo 1 a mais em sua quantidade
            ocorrencias[numeros[i]] += 1
            
    for k in ocorrencias.keys(): #Para cada valor armazenado no dicionário, verifico qual deles tem um número de ocorrências ímpar (ou seja, que não consigo formar pares)
        if ocorrencias[k] % 2 != 0: 
            print(k)
            break #Como só tem um único valor sem par, então basta imprimir ele e sair fora do loop