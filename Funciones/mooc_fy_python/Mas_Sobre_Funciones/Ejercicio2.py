def maximo(a,b,c):
    if a >= b and a >= c:
        print(f'El numero {a} (a), es mayor que {b} (b), y que {c} (c)')
    else:
        if b >= c:
            print(f'El numero {b} (b), es mayor que {a} (a), y que {c} (c)')
        else:
            print(f'El numero {c} (c), es mayor que {b} (b), y que {a} (a)')


maximo(3,4,5)
maximo(3,5,4)
maximo(5,4,3)