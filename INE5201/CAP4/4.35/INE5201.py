import turtle

# Função para determinar a posição do ponto p2
def determine_position(p0, p1, p2):
    # Usamos a fórmula da equação da reta para determinar se p2 está à esquerda, à direita ou na reta
    # A fórmula é: (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2

    result = (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)

    if result > 0:
        return 'à esquerda'
    elif result < 0:
        return 'à direita'
    else:
        return 'sobre a linha'

# Função para desenhar os pontos e a linha usando turtle
def draw_graph(p0, p1, p2, position):
    screen = turtle.Screen()
    screen.setworldcoordinates(-100, -100, 100, 100)  # Define o limite da janela de visualização

    t = turtle.Turtle()
    t.speed(0)  # Desenha rapidamente

    # Desenhar a linha de p0 a p1
    t.penup()
    t.goto(p0)
    t.pendown()
    t.goto(p1)

    # Desenhar o ponto p2
    t.penup()
    t.goto(p2)
    t.dot(10, 'red')  # Desenha o ponto p2 em vermelho

    # Exibir a posição de p2
    t.penup()
    t.goto(0, -50)
    t.write(f'p2 está {position} da linha.', align='center', font=('Arial', 12, 'normal'))

    turtle.done()

# Função principal
def main():
    # Solicitar as coordenadas dos pontos ao usuário
    x0, y0 = map(int, input('Digite as coordenadas de p0 (x0 y0): ').split(", "))
    x1, y1 = map(int, input('Digite as coordenadas de p1 (x1 y1): ').split(", "))
    x2, y2 = map(int, input('Digite as coordenadas de p2 (x2 y2): ').split(", "))

    # Determinar a posição de p2
    position = determine_position((x0, y0), (x1, y1), (x2, y2))

    # Desenhar o gráfico e exibir a posição de p2
    draw_graph((x0, y0), (x1, y1), (x2, y2), position)