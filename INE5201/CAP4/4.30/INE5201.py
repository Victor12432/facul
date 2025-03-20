import time

def main():
    # Obtém o tempo atual em segundos desde a época
    total_seconds = time.time()
    
    # Converte o tempo em horas, minutos e segundos
    current_time = time.gmtime(total_seconds)
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Solicita ao usuário o deslocamento em relação ao horário GMT
    offset = int(input('Enter the time zone offset to GMT: '))

    # Ajusta a hora com base no deslocamento do fuso horário
    hour = (hour + offset) % 24
    
    # Determinando se é AM ou PM
    period = 'AM' if hour < 12 else 'PM'
    
    # Convertendo a hora para o formato de 12 horas
    hour = hour % 12
    hour = 12 if hour == 0 else hour  # Corrige caso a hora seja 0 para 12

    # Exibindo a hora no formato ajustado
    print('The current time is %02d:%02d:%02d %s' % (hour, minute, second, period))
