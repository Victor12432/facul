def main():
    # Constantes para conversão
    POUNDS_TO_KILOGRAMS = 0.45359237
    INCHES_TO_METERS = 0.0254

    # Solicitar peso e altura do usuário
    weight_pounds = float(input('Enter weight in pounds: '))
    height_feet = int(input('Enter feet: '))
    height_inches = int(input('Enter inches: '))

    # Converter peso para quilogramas
    weight_kg = weight_pounds * POUNDS_TO_KILOGRAMS

    # Converter altura total para metros
    total_inches = (height_feet * 12) + height_inches
    height_meters = total_inches * INCHES_TO_METERS
    # Calcular o BMI (IMC)
    bmi = weight_kg / (height_meters ** 2)

    # Exibir o resultado com uma mensagem adequada
    print('BMI is %f' % bmi)

    if bmi < 18.5:
        print('You are Underweight')
    elif bmi >= 18.5 and bmi < 25:
        print('You are Normal')
    elif bmi >= 25 and bmi < 30:
        print('You are Overweight')
    else:
        print('You are Obesity')

