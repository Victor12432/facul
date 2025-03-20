import random

def pick_a_card():
    # Definindo os naipes e os valores das cartas
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    # Sorteando um naipe e um valor de carta
    suit = random.choice(suits)
    rank = random.choice(ranks)
    
    # Exibindo a carta sorteada
    print('The card you picked is the %s of %s' % (rank, suit))

def main():
    pick_a_card()

