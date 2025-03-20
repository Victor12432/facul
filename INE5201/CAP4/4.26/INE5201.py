def is_palindrome(num):
    # Convertendo o número para uma string
    num_str = str(num)
    
    # Verificando se o número é igual ao seu reverso
    if num_str == num_str[::-1]:
        return True
    else:
        return False

def main():
    # Solicita ao usuário um número de três dígitos
    num = int(input('Enter a three-digit integer: '))
    
    # Verifica se o número é um palíndromo
    if 100 <= num <= 999:  # Verifica se o número é de 3 dígitos
        if is_palindrome(num):
            print('%d is a palindrome number.' % num)
        else:
            print('%d is not a palindrome number.' % num)
    else:
        print('Please enter a valid three-digit number.')