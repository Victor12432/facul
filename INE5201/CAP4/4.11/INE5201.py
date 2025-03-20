def is_leap_year(year):
    # Função para verificar se o ano é bissexto
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    # Verifica o número de dias de acordo com o mês e o ano
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 'Month not exist!'

def main():
    # Solicita ao usuário o mês e o ano
    month = int(input('Enter with the month: '))
    year = int(input('Enter with the year: '))

    # Obtém o número de dias no mês
    days = days_in_month(month, year)

    if days == 'Month not exist!':
        print('Month not exist !. please, enter with a number between 1 at 12.')
    else:
        # Exibe o resultado
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']
        print('%s %d has %d days.' % (month_names[month-1], year, days))


