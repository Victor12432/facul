x = int(input())
while True:
    if x < 0 or x > 10:
        print('incorrect')
        x = int(input())
    else:
        print('The number is', x)
        break