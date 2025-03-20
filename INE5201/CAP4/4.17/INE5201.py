import random

def play_game():
    # Dicionário para mapear os números para as opções
    options = {0: 'scissor', 1: 'rock', 2: 'paper'}
    
    # O computador escolhe aleatoriamente entre 0, 1 e 2
    computer_choice = random.randint(0, 2)
    
    # Solicita ao usuário para escolher entre 0, 1 ou 2
    user_choice = int(input('scissor (0), rock (1), paper (2): '))
    
    # Exibe as escolhas do usuário e do computador
    
    # Lógica para determinar o vencedor
    if user_choice == computer_choice:
        print('The computer is %s. You are %s too. It is a draw.Empate!' % (options[computer_choice], options[user_choice]))
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print('The computer is %s. You are %s. You lost.' % (options[computer_choice], options[user_choice]))
    else:
        print('The computer is %s. You are %s. You won.' % (options[computer_choice], options[user_choice]))

def main():
    play_game()

