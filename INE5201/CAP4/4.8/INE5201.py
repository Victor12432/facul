def main():
    # Solicita três números inteiros do usuário
    num1 = int(input('Enter with the first number: '))
    num2 = int(input('Enter with the second number: '))
    num3 = int(input('Enter with the third number: '))

    # Coloca os números em uma lista
    numbers = [num1, num2, num3]

    # Ordena a lista em ordem crescente
    numbers.sort()

    # Exibe os números ordenados
    print('The order is:', numbers[0], numbers[1], numbers[2])


