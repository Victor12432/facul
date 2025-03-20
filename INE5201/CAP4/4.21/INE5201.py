import math

def zellers_congruence():
    # Solicita ao usuário o ano, mês e dia
    year = int(input('Enter year: (e.g., 2008): '))
    month = int(input('Enter month: 1-12: '))
    day = int(input('Enter the day of the month: 1-31: '))
    
    # Ajusta o mês e o ano para janeiro e fevereiro
    if month == 1 or month == 2:
        month += 12
        year -= 1
    
    # Calcula o século (j) e o ano do século (k)
    j = math.trunc(year // 100)  # Século
    k = year % 100   # Ano do século
    
    # Aplica a fórmula de Zeller
    h = (day + math.trunc((13 * (month + 1)) // 5) + k + math.trunc(k // 4) + math.trunc(j // 4) + 5 * j) % 7
    
    # Mapear os valores de h para os nomes dos dias da semana
    days_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    # Exibe o dia da semana
    print('Day of the week is ' + days_week[h])

def main():
    zellers_congruence()

main()
