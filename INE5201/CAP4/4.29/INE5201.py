import math

def check_circles(x1, y1, r1, x2, y2, r2):
    '''
    Verifica a relação entre dois círculos:
    - (x1, y1), r1: centro e raio do primeiro círculo.
    - (x2, y2), r2: centro e raio do segundo círculo.
    '''
    # Calcula a distância entre os centros dos dois círculos
    distance = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
    
    # Verifica se o círculo 2 está dentro do círculo 1
    if distance <= abs(r1 - r2):
        return 'circle2 is inside circle1'
    
    # Verifica se os círculos se sobrepõem
    elif distance <= (r1 + r2):
        return 'circle2 overlaps circle1'
    
    # Caso contrário, os círculos não se tocam
    else:
        return 'circle2 does not overlap circle1'

# Entrada do usuário
print('Digite as coordenadas do centro e o raio do primeiro círculo:')
x1, y1, r1 = map(float, input('Enter circle1s center x-, y-coordinates, and radius: ').split(", "))
x2, y2, r2 = map(float, input('Enter circle2s center x-, y-coordinates, and radius: ').split(", "))


# Resultado
resultado = check_circles(x1, y1, r1, x2, y2, r2)
print('\n' + resultado)