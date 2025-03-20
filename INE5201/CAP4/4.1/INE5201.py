import math


def Result(a, b, c):
    return math.pow(b, 2) - 4 * a * c


def Prompt(s1, a, b):
    if s1 == 0:
        raiz = -b/(2*a)
        print('The roots is %.6f' % raiz)
    elif s1 > 0:
        sqrts = math.sqrt(s1)
        raiz1 = ((-b)+sqrts)/(2*a)
        sqrts = math.sqrt(s1)
        raiz2 = ((-b)-sqrts)/(2*a)
        print('The roots are %.6f and %.6f' % (raiz1, raiz2))
    else:
        print('The equation has no real roots')


def main():
    a, b, c = map(float, input('Enter , c: ').split(", "))
    s1 = Result(a, b, c)
    Prompt(s1, a, b)