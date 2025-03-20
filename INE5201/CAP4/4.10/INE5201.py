import random

def main():
    # Gera dois números aleatórios menores que 100
    number1 = random.randint(0, 99)
    number2 = random.randint(0, 99)

    # Solicita ao usuário a resposta para a multiplicação
    answer = int(input('What is %d x %d? ' % (number1, number2)))

    # Verifica se a resposta está correta
    if answer == number1 * number2:
        print('Congratulations! The sum is correct.')
    else:
        print('Oh No! The correct response is %d' % (number2*number1))

