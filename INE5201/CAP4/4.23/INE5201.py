def check_point_in_rectangle():
    # Solicita ao usuário as coordenadas x e y no formato: "x, y"
    x, y = map(float, input('Enter a point with two coordinates: ').split(", "))

    # Dimensões do retângulo
    width = 10
    height = 5

    # Verifica se o ponto está dentro do retângulo
    if abs(x) <= width / 2 and abs(y) <= height / 2:
        print('Point (%.1f, %.1f) is in the rectangle' % (x, y))
    else:
        print('Point (%.1f, %.1f) is not in the rectangle' % (x, y))

def main():
    check_point_in_rectangle()