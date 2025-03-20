def main():
    # Solicitar os valores de a, b, c, d, e, f
    a, b, c, d, e, f = map(float, input('Enter a, b, c, d, e, f: ').split(", "))
        

    # Calcular o denominador
    denominator = (a * d) - (b * c)

    # Verificar se a equação tem solução
    if denominator == 0:
        print('The equation has no solution.')
    else:
        # Usar a regra de Cramer para calcular x e y
        x = (e * d - b * f) / denominator
        y = (a * f - e * c) / denominator
        print('x = %.1f and y = %.1f' % (x, y))


