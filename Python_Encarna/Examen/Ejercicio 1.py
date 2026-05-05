#di si la temperatura es fria o agradable, si es menor a 15 grados es fria, si no es agradable

def temperatura():
    temperatura = int(input("Dime una temperatura: "))

    if temperatura < 15:
        print('frio')
    else:
        print('Agradable')
    
temperatura()
