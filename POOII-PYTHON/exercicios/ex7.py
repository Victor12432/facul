import random

x = []

for i in range(5):
    x.append(random.randint(0, 10000))
x.sort(reverse=True)
print(x[0])