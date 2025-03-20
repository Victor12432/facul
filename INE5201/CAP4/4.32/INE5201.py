def point_position(x0, y0, x1, y1, x2, y2):
    '''
    Função para determinar se um ponto está à esquerda, direita ou sobre uma linha.
    
    Parâmetros:
    p0 : tuple - Coordenadas do ponto inicial da linha (x0, y0).
    p1 : tuple - Coordenadas do ponto final da linha (x1, y1).
    p2 : tuple - Coordenadas do ponto a ser testado (x2, y2).
    
    Retorno:
    str - Indicação da posição do ponto p2 em relação à linha direcionada.
    '''

    # Cálculo do determinante
    determinant = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    
    # Determinação da posição do ponto
    if determinant > 0:
        return ('(%.1f, %.1f) is on the left side of the line from (%.1f, %.1f) to (%.1f, %.1f)' % (x2, y2, x0, y0, x1, y1))
    elif determinant < 0:
        return ('(%.1f, %.1f) is on the right side of the line from (%.1f, %.1f) to (%.1f, %.1f)' % (x2, y2, x0, y0, x1, y1))
    else:
        return ('(%.1f, %.1f)is on the same line from (%.1f, %.1f) to (%.1f, %.1f)' % (x2, y2, x0, y0, x1, y1))

def main():
    # Entrada do usuário para as coordenadas dos pontos
    print('Enter coordinates for the three points p0, p1, and p2:')
    x0, y0, x1, y1, x2, y2 = map(float, input().split(", "))
    
    # Chama a função e exibe o resultado
    resultado = point_position(x0, y0, x1, y1, x2, y2)
    print(resultado)