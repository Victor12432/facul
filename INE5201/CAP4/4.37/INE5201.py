import turtle

# Função para verificar se o ponto está dentro do retângulo
def is_inside_rectangle(x, y, width, height):
    return -width/2 <= x <= width/2 and -height/2 <= y <= height/2

# Função principal
def main():
    # Configurações da tela do Turtle
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    
    # Cria uma tartaruga para desenhar
    t = turtle.Turtle()
    t.speed(0)  # Define a velocidade máxima para desenhar
    
    # Solicitar entrada do usuário para as coordenadas do ponto
    x = float(screen.numinput('Ponto', 'Digite a coordenada x do ponto: '))
    y = float(screen.numinput('Ponto', 'Digite a coordenada y do ponto: '))
    
    # Definir as dimensões do retângulo
    width = 100
    height = 50
    
    # Desenhar o retângulo centrado na origem (0, 0)
    t.penup()
    t.goto(-width/2, height/2)  # Posiciona no canto superior esquerdo
    t.pendown()
    for _ in range(2):  # Desenha o retângulo
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    
    # Desenhar o ponto inserido pelo usuário
    t.penup()
    t.goto(x, y)
    t.dot(10, 'red')  # Desenha o ponto como um círculo vermelho
    
    # Verificar se o ponto está dentro do retângulo
    if is_inside_rectangle(x, y, width, height):
        t.goto(0, -100)
        t.write('O ponto está dentro do retângulo.', align='center', font=('Arial', 16, 'normal'))
    else:
        t.goto(0, -100)
        t.write('O ponto está fora do retângulo.', align='center', font=('Arial', 16, 'normal'))
    
    # Finalizar
    t.hideturtle()
    screen.mainloop()  # Mantém a janela aberta