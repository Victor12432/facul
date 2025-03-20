def decimal_to_hex(decimal):
    # Converte o número decimal para hexadecimal usando a função hex()
    hex_value = hex(decimal)
    # Retorna o valor hexadecimal sem o prefixo '0x'
    return hex_value[2:].upper()

def main():
    # Solicita ao usuário um número inteiro entre 0 e 15
    decimal = int(input('Enter a decimal value (0 to 15): '))
    
    # Verifica se o número está dentro do intervalo válido
    if 0 <= decimal <= 15:
        hex_value = decimal_to_hex(decimal)
        print('The hex value is ' + hex_value)
    else:
        print('Invalid input')