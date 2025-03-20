name, key = input().split()
name, key = str(name), str(key)

while True:
    if name == key:
        print('The key = a the userName, informen new key')
        key = str(input())
    else:
        print('PASS')
        break