import math

def wind_chill():
    # Solicita ao usuário a temperatura e a velocidade do vento
    temperature = float(input('Digite a temperatura em Fahrenheit (°F): '))
    wind_speed = float(input('Digite a velocidade do vento em milhas por hora (mph): '))
    
    # Verifica se os valores estão dentro do intervalo válido
    if temperature >= -58 and temperature <= 41 and wind_speed >= 2:
        # Calcula a sensação térmica (wind-chill)
        wind_chill_temperature = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
        print('A temperatura de sensação térmica (wind-chill) é: %.2f°F' % wind_chill_temperature)
    else:
        # Exibe uma mensagem de erro caso os valores não sejam válidos
        if temperature < -58 or temperature > 41:
            print('Temperatura inválida. A temperatura deve estar entre 41°F e 58°F.')
        if wind_speed < 2:
            print('Velocidade do vento inválida. A velocidade do vento deve ser maior ou igual a 2 mph.')

def main():
    wind_chill()

