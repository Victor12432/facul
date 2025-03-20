name, age, pay, gender, status = input('Enter with name, age, pay, gender, status: \n').split()
name, age, pay, gender, status = str(name), int(age), float(pay), str(gender), str(status)

while True:
    if len(name) < 3:
        name = input('Enter a new valid name: ')
    elif age < 0 or age > 150:
        age = int(input('Enter a new valid age: '))
    elif pay < 0:
        pay = float(input('Enter a new valid pay: '))
    elif not(gender == 'f' or gender == 'm'):
        gender = input('Enter a new valid gender ( f or m): ')
    elif not(status == 's' or status == 'c' or status == 'v' or status == 'd'):
        status = input('Enter a new valid status (s, c, v or d): ')
    else:
        print('Correct goob boy')
        break