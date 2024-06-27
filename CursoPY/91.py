import random
import time
import operator
jogo = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6)
}
rank = dict()
rank = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('Valores sorteador:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
print('-='*30)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')