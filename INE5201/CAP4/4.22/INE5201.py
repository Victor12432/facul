import math

# Função para verificar se o ponto está no círculo
def is_point_in_circle(x, y, radius=10):
    distance = math.sqrt(x**2 + y**2)
    return distance <= radius

# Entrada do usuário
def main():
    x, y = map(float, input('Enter a point with two coordinates ').split(", "))

    # Verificação
    if is_point_in_circle(x, y):
        print('Point (%.1f, %.1f) is in the circle' % (x, y))
    else:
        print('Point (%.1f, %.1f) is not in the circle' % (x, y))
main()