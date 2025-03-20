import turtle

# Função para desenhar um retângulo
def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x - width / 2, y + height / 2)  # Posiciona o pen no canto superior esquerdo
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):  # Desenha o retângulo
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()

# Função para verificar se o segundo retângulo está dentro do primeiro
def is_inside(rect1, rect2):
    x1, y1, w1, h1 = rect1  # Centro e dimensões do primeiro retângulo
    x2, y2, w2, h2 = rect2  # Centro e dimensões do segundo retângulo
    
    # Verifica se todos os lados do segundo retângulo estão dentro do primeiro
    return (x2 - w2 / 2 >= x1 - w1 / 2 and x2 + w2 / 2 <= x1 + w1 / 2 and
            y2 - h2 / 2 >= y1 - h1 / 2 and y2 + h2 / 2 <= y1 + h1 / 2)

# Função para verificar se os dois retângulos se sobrepõem
def is_overlap(rect1, rect2):
    x1, y1, w1, h1 = rect1  # Centro e dimensões do primeiro retângulo
    x2, y2, w2, h2 = rect2  # Centro e dimensões do segundo retângulo
    
    # Verifica se não há sobreposição (retângulos não se tocam)
    return not (x2 + w2 / 2 <= x1 - w1 / 2 or x2 - w2 / 2 >= x1 + w1 / 2 or
                y2 + h2 / 2 <= y1 - h1 / 2 or y2 - h2 / 2 >= y1 + h1 / 2)

# Função principal
def main():
    screen = turtle.Screen()
    screen.setworldcoordinates(-300, -300, 300, 300)  # Ajusta as coordenadas do mundo para o centro
    t = turtle.Turtle()
    t.speed(0)

    # Solicita as entradas do usuário para os dois retângulos
    x1, y1, w1, h1 = map(float, input('Digite o centro x, y, a largura e a altura do primeiro retângulo (x1 y1 w1 h1): ').split(", "))
    x2, y2, w2, h2 = map(float, input('Digite o centro x, y, a largura e a altura do segundo retângulo (x2 y2 w2 h2): ').split(", "))

    # Desenha os retângulos
    draw_rectangle(t, x1, y1, w1, h1, "blue")  # Retângulo 1 (azul)
    draw_rectangle(t, x2, y2, w2, h2, "red")   # Retângulo 2 (vermelho)

    # Verifica se o segundo retângulo está dentro do primeiro ou se há sobreposição
    if is_inside((x1, y1, w1, h1), (x2, y2, w2, h2)):
        print('O segundo retângulo está dentro do primeiro retângulo.')
    elif is_overlap((x1, y1, w1, h1), (x2, y2, w2, h2)):
        print('O segundo retângulo se sobrepõe com o primeiro retângulo.')
    else:
        print('O segundo retângulo não se sobrepõe com o primeiro retângulo.')

    turtle.done()  # Finaliza o desenho