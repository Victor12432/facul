'''
O programa recebe o intervalo de Tempo (T) em horas e a
velocidade média durante o intervalo (V) em km/h,
realiza o produto dos 2 valores e ao final imprime
a distância total percorrida.
'''
vel = 0

for i in range(1, int(input())+1):
    T, V = input().split()
    T, V = int(T), int(V)

vel += T*V

print(vel)
