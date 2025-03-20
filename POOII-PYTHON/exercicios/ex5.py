a = int(input('Enter a: '))
taxaA = int(input('Enter taxaA: '))/100
b = int(input('Enter b: '))
taxaB = int(input('Enter taxaB: '))/100
year = 0

while a < b:
    a += a*taxaA
    b += b*taxaB
    year += 1
print(year)