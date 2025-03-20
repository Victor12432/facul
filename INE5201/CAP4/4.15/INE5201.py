import random

def lottery():
    # Gera um número aleatório de 3 dígitos
    lottery_number = random.randint(100, 999)
    
    # Solicita ao usuário que insira um número de 3 dígitos
    user_input = int(input('Digite um número de 3 dígitos para tentar a sorte na loteria: '))
    
    # Converte os números para listas de dígitos para comparar facilmente
    lottery_digits = [int(digit) for digit in str(lottery_number)]
    user_digits = [int(digit) for digit in str(user_input)]
    
    # Verifica se o número do usuário é igual ao número da loteria (regra 1)
    if user_input == lottery_number:
        print('Você ganhou! O número da loteria é {lottery_number}. Seu prêmio é $10,000.')
    # Verifica se todos os dígitos do usuário coincidem com os dígitos da loteria, mas em ordem diferente (regra 2)
    elif sorted(user_digits) == sorted(lottery_digits):
        print('Você ganhou! O número da loteria é {lottery_number}. Seu prêmio é $3,000.')
    # Verifica se pelo menos um dígito do usuário coincide com a loteria (regra 3)
    elif any(digit in lottery_digits for digit in user_digits):
        print('Você ganhou! O número da loteria é {lottery_number}. Seu prêmio é $1,000.')
    else:
        print('Você não ganhou. O número da loteria era {lottery_number}.')

def main():
    lottery()

