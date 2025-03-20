a = 80000
taxaA = 0.03
b = 200000
taxaB = 0.015
year = 0

while a < b:
    a += a*taxaA
    b += b*taxaB
    year += 1
print(year)