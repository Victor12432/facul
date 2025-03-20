def hex_to_decimal(hex_char):
    # Converte o caractere hexadecimal para decimal
    decimal_value = int(hex_char, 16)
    return decimal_value

def main():
    # Solicita ao usuário um caractere hexadecimal (0-9 ou A-F)
    hex_char = input('Enter a hex character: ').upper()
    
    # Verifica se o caractere é válido
    if hex_char in '0123456789ABCDEF' and len(hex_char) == 1:
        decimal_value = hex_to_decimal(hex_char)
        print('The decimal value is ' + str(decimal_value))
    else:
        print('Invalid input')