# Função para calcular a área de um triângulo usando a fórmula de Heron
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# Função para verificar se um ponto está dentro do triângulo
def is_inside_triangle(px, py):
    # Coordenadas dos vértices do triângulo
    x1, y1 = 0, 0
    x2, y2 = 200, 0
    x3, y3 = 0, 100

    # Calcula a área do triângulo original
    A = area(x1, y1, x2, y2, x3, y3)

    # Calcula as áreas dos subtriângulos formados pelo ponto e os vértices
    A1 = area(px, py, x2, y2, x3, y3)
    A2 = area(x1, y1, px, py, x3, y3)
    A3 = area(x1, y1, x2, y2, px, py)

    # Verifica se a soma das áreas dos subtriângulos é igual à área original
    return abs(A - (A1 + A2 + A3)) < 1e-9  # Verificação com tolerância para evitar problemas de precisão

# Entrada do usuário
def main():
    x, y = map(float, input('Enter a points x- and y-coordinates: ').split(", "))

    # Verifica se o ponto está dentro do triângulo
    if is_inside_triangle(x, y):
        print('The point is in the triangle')
    else:
        print('The point is not in the triangle')