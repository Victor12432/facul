def currency_exchange():
    # Solicita ao usuário a taxa de câmbio entre USD e RMB
    exchange_rate = float(input('Enter the exchange rate from dollars to RMB: '))
    
    # Solicita ao usuário escolher a direção da conversão
    conversion_type = int(input('Enter 0 to convert dollars to RMB and 1 vice versa: '))
    
    if conversion_type == 0:
        # Converte de USD para RMB
        usd_amount = float(input('Enter the dollar amount: '))
        rmb_amount = usd_amount * exchange_rate
        print('$%.2f is %.2f yuan' % (usd_amount, rmb_amount))
    elif conversion_type == 1:
        # Converte de RMB para USD
        rmb_amount = float(input('Digite o valor em Renminbi chinês (RMB) que você deseja converter: '))
        usd_amount = rmb_amount / exchange_rate
        print('%.2f yuan is $%.2f' % (rmb_amount, usd_amount))
    else:
        print('Incorrect input')

def main():
    currency_exchange()

