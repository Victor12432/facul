def main():
    # Solicita ao usuário o valor em centavos
    amount = int(input('What pennies in your bag? '))

    # Verifica se o valor informado é menor ou igual a zero
    if amount <= 0:
        print('Fool, not has pennies to count')
    # Converte o valor em centavos para as unidades monetárias
    dollars = amount // 100
    remaining_amount = amount % 100

    quarters = remaining_amount // 25
    remaining_amount = remaining_amount % 25

    dimes = remaining_amount // 10
    remaining_amount = remaining_amount % 10

    nickels = remaining_amount // 5
    remaining_amount = remaining_amount % 5

    pennies = remaining_amount

    # Cria uma lista para armazenar os resultados formatados
    result = []

    # Adiciona as denominações com singular ou plural
    if dollars > 0:
        result.append(str(dollars) + ' ' + 'dollar' + ('s' if dollars != 1 else ''))
    if quarters > 0:
        result.append(str(quarters) + ' ' + 'quarter' + ('s' if quarters != 1 else ''))
    if dimes > 0:
        result.append(str(dimes) + ' ' + 'dime' + ('s' if dimes != 1 else ''))
    if nickels > 0:
        result.append(str(nickels) + ' ' + 'nickel' + ('s' if nickels != 1 else ''))
    if pennies > 0:
        result.append(str(pennies) + ' ' + 'penn' + ('ies' if pennies != 1 else 'y'))

    # Exibe as denominações não nulas
    print('You have: ')
    print(', '.join(result))


