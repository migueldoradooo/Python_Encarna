num = int(input('Introduce un numero: '))
suma = 0 


while True:
    if num!=0:
        num = int(input('Introduce un numero(si quieres dejar de sumar, pon 0): '))
        suma = suma + num
    else:
        break;

print('Suma total: ' , suma)