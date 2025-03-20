def main():
    # Nomes dos dias da semana
    days_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
                      'Thursday', 'Friday', 'Saturday']
    
    # Solicitar o dia atual e o número de dias no futuro
    today = int(input('Enter todays day: '))
    days_future = int(input('Enter the number of days elapsed since today: '))

    # Calcular o dia futuro
    future = (today + days_future) % 7

    # Exibir os resultados
    print('Today is %s and the future day is %s' % (days_week[today], days_week[future]))


