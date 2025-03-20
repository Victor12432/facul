import random

def heads_or_tails():
    # Gera aleatoriamente 0 (cara) ou 1 (coroa)
    result = random.randint(0, 1)
    coin = ['Cara', 'Coroa']
    # Solicita ao usuário para adivinhar
    guess = input('Adivinhe o resultado da moeda (cara ou coroa): ').strip().lower()
    
    # Verifica se o palpite está correto
    if guess == coin[result]:
        print('Você acertou! O resultado foi %s.' % coin[result])
    else:
        print('Você errou. O resultado foi %s.' % coin[result] )

def main():
    heads_or_tails()

