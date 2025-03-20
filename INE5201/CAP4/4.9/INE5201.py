def main():
    # Solicita os dados da primeira embalagem
    weight1, price1 = map(float, input('Enter weight and price for package 1: ').split(", "))
    

    # Solicita os dados da segunda embalagem
    weight2, price2 = map(float, input('Enter weight and price for package 2: ').split(", "))
    

    # Calcula o preço por unidade de peso (custo por kg)
    cost1 = weight1 / price1
    cost2 = weight2 / price2

    # Compara os custos e determina a melhor opção
    if cost1 < cost2:
        print('\nPackage 1 has the better price.')
    elif cost1 > cost2:
        print('\nPackage 2 has the better price.')
    else:
        print('\nSame priece.')


