# Função para calcular o ponto de interseção entre duas linhas
def intersecting_point(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculando os determinantes
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    # Verificando se as linhas são paralelas
    if denominator == 0:
        return None  # Linhas paralelas, sem ponto de interseção
    
    # Calculando os numeradores
    px_numerator = ((x1 * y2 - y1 * x2) * (x3 - x4)) - ((x1 - x2) * (x3 * y4 - y3 * x4))
    py_numerator = ((x1 * y2 - y1 * x2) * (y3 - y4)) - ((y1 - y2) * (x3 * y4 - y3 * x4))
    
    # Calculando as coordenadas do ponto de interseção
    px = px_numerator / denominator
    py = py_numerator / denominator
    
    return px, py
def main():
# Entrada do usuário
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input('Enter x1, y1, x2, y2, x3, y3, x4, y4: ').split(", "))
    # Cálculo do ponto de interseção
    result = intersecting_point(x1, y1, x2, y2, x3, y3, x4, y4)

    # Exibindo o resultado
    if result:
        print('The intersecting point is at: (%.2f, %.2f)' % (result[0], result[1]))
    else:
        print('The two lines are parallel')