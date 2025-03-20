def check_rectangle_overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    '''
    Verifica a relação entre dois retângulos.
    (x1, y1): centro do primeiro retângulo (w1, h1)
    (x2, y2): centro do segundo retângulo (w2, h2)
    '''
    # Coordenadas dos limites do retângulo 1
    left1 = x1 - w1 / 2
    right1 = x1 + w1 / 2
    top1 = y1 + h1 / 2
    bottom1 = y1 - h1 / 2

    # Coordenadas dos limites do retângulo 2
    left2 = x2 - w2 / 2
    right2 = x2 + w2 / 2
    top2 = y2 + h2 / 2
    bottom2 = y2 - h2 / 2

    # Verifica se o segundo retângulo está completamente dentro do primeiro
    if (left2 >= left1 and right2 <= right1 and 
        top2 <= top1 and bottom2 >= bottom1):
        return 'r2 is inside r1'

    # Verifica se os retângulos se sobrepõem
    if not (right1 < left2 or left1 > right2 or top1 < bottom2 or bottom1 > top2):
        return 'r2 overlaps r1'

    # Caso contrário, não há sobreposição
    return 'r2 does not overlap r1'

# Entrada do usuário
def main():
    x1, y1, w1, h1 = map(float, input('Enter r1s center x-, y-coordinates, width, and height: ').split(", "))
    x2, y2, w2, h2 = map(float, input('Enter r2s center x-, y-coordinates, width, and height: ').split(", "))

    # Resultado
    resultado = check_rectangle_overlap(x1, y1, w1, h1, x2, y2, w2, h2)
    print('\n' + resultado)