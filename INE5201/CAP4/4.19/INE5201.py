def compute_perimeter():
    # Solicita ao usuário os três lados do triângulo
    a, b, c = map(float, input('Enter three edges: ').split(", "))
    
    # Verifica se a soma de dois lados é maior que o terceiro para todos os pares
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        print('The perimeter is ' + str(perimeter))
    else:
        print('The input is invalid')

def main():
    compute_perimeter()

