import random

def main():
    # Gerar três números inteiros de um dígito aleatoriamente
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    
    # Exibir os números gerados e solicitar a soma
    print('The numbres generate is : %d, %d and %d' % (num1, num2, num3))
    user_sum = int(input('What is the sum of the three digits: '))
    
    # Verificar se a soma está correta
    correct_sum = num1 + num2 + num3
    if user_sum == correct_sum:
        print('Congratulations! The sum is correct.')
    else:
        print('Oh No! The correct response is %d' % correct_sum)



