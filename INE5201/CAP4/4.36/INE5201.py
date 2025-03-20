import turtle
import random
import math

# Função para verificar se o ponto está dentro do círculo
def is_inside_circle(x, y, radius):
    return x**2 + y**2 <= radius**2

# Função principal
def main():
    # Configurações da tela do Turtle
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    
    # Cria uma tartaruga para desenhar
    t = turtle.Turtle()
    t.speed(0)  # Define a velocidade máxima para desenhar

    # Definir o raio do círculo
    radius = 200
    
    # Desenhar o círculo
    t.penup()
    t.goto(0, -radius)  # Vai até a posição inicial para desenhar o círculo
    t.pendown()
    t.circle(radius)  # Desenha o círculo com o raio especificado
    
    # Gerar um ponto aleatório dentro do quadrado
    # O quadrado tem o mesmo centro do círculo e o lado igual ao diâmetro do círculo
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    
    # Desenhar o ponto aleatório
    t.penup()
    t.goto(x, y)
    t.dot(10, 'red')  # Desenha o ponto como um círculo vermelho de tamanho 10
    
    # Verificar se o ponto está dentro do círculo
    if is_inside_circle(x, y, radius):
        t.goto(0, 250)
        t.write('O ponto está dentro do círculo.', align='center', font=('Arial', 16, 'normal'))
    else:
        t.goto(0, 250)
        t.write('O ponto está fora do círculo.', align='center', font=('Arial', 16, 'normal'))
    
    # Finalizar
    t.hideturtle()
    screen.mainloop()  # Mantém a janela aberta
