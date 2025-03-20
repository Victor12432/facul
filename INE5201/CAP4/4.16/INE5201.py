import random
import string

def random_uppercase_letter():
    # Gera uma letra maiúscula aleatória
    letter = random.choice(string.ascii_uppercase)
    print('A letra maiúscula aleatória é: %s' % letter)

def main():
    random_uppercase_letter()

