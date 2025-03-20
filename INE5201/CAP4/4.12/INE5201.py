def main():
    # Solicita ao usuário um número inteiro
    number = int(input('Enter an integer: '))

    divisible5 = (True if number % 5 == 0 else False)
    divisible6 = (True if number % 6 == 0 else False)
    
    if divisible6 and divisible5:
         print('Is %d divisible by 5 and 6? True' % number)
    else:
        print('Is %d divisible by 5 and 6? False' % number)
    
    if divisible6 or divisible5:
        print('Is %d divisible by 5 or 6? True' % number)
    else:
        print('Is %d divisible by 5 and 6? False' % number)

    if (divisible6 and (not divisible5)) or ((not divisible6) and divisible5):
        print('Is %d divisible by 5 or 6, but not both? True' % number)
    else:
        print('Is %d divisible by 5 or 6, but not both? False' % number)

