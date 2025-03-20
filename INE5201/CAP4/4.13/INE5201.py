def compute_tax(income, status):
    # Faixa de imposto para Solteiros
    if status == 'solteiro':
        if income <= 9700:
            tax = income * 0.10
        elif income <= 39475:
            tax = 970 + (income - 9700) * 0.12
        elif income <= 84200:
            tax = 4543 + (income - 39475) * 0.22
        elif income <= 160725:
            tax = 14382.50 + (income - 84200) * 0.24
        elif income <= 204100:
            tax = 32748.50 + (income - 160725) * 0.32
        elif income <= 510300:
            tax = 46628.50 + (income - 204100) * 0.35
        else:
            tax = 153798.50 + (income - 510300) * 0.37
    # Faixa de imposto para Casados e juntos
    elif status == 'casado_juntos':
        if income <= 19400:
            tax = income * 0.10
        elif income <= 78950:
            tax = 1940 + (income - 19400) * 0.12
        elif income <= 168400:
            tax = 9086 + (income - 78950) * 0.22
        elif income <= 321450:
            tax = 28765 + (income - 168400) * 0.24
        elif income <= 408200:
            tax = 64285 + (income - 321450) * 0.32
        elif income <= 612350:
            tax = 93947 + (income - 408200) * 0.35
        else:
            tax = 164219 + (income - 612350) * 0.37
    # Faixa de imposto para Casados mas separados
    elif status == 'casado_separado':
        if income <= 9700:
            tax = income * 0.10
        elif income <= 39475:
            tax = 970 + (income - 9700) * 0.12
        elif income <= 84200:
            tax = 4543 + (income - 39475) * 0.22
        elif income <= 160725:
            tax = 14382.50 + (income - 84200) * 0.24
        elif income <= 204100:
            tax = 32748.50 + (income - 160725) * 0.32
        elif income <= 510300:
            tax = 46628.50 + (income - 204100) * 0.35
        else:
            tax = 153798.50 + (income - 510300) * 0.37
    # Faixa de imposto para chefes de familia
    elif status == 'chefe_familia':
        if income <= 13850:
            tax = income * 0.10
        elif income <= 52850:
            tax = 1385 + (income - 13850) * 0.12
        elif income <= 84200:
            tax = 6163 + (income - 52850) * 0.22
        elif income <= 160700:
            tax = 13087 + (income - 84200) * 0.24
        elif income <= 204100:
            tax = 32347 + (income - 160700) * 0.32
        elif income <= 510300:
            tax = 46347 + (income - 204100) * 0.35
        else:
            tax = 153798.50 + (income - 510300) * 0.37
    else:
        return 'Status de declaração inválido.'

    return tax


def main():
    # Solicita o status de declaração e a renda
    status = input('Digite o seu status de declaração (solteiro, casado_juntos, casado_separado, chefe_familia): ').strip().lower()
    income = float(input('Digite sua renda anual: R$ '))

    # Calcula o imposto
    tax = compute_tax(income, status)

    # Exibe o imposto calculado
    print('O imposto a ser pago é: R$ %.2f' % tax)


