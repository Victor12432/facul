import random

def main():
    # Gerar dois números inteiros aleatórios menores que 100
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    
    # Mostrar os números e pedir a soma
    print('What is {num1} + {num2}?')
    user_answer = int(input('Sum: '))
    
    # Verificar se a resposta está correta
    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print('True')
    else:
        print('False\nThe correct response is %d' % correct_answer)

