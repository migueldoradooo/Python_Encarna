#Adivinar con pistas

num = 3
adi= int(input('Ingresa un numero: '))

while adi < num or adi > num:
    if adi < num:
        print('Demasiado Bajo')
        adi= int(input('Ingresa un numero otra vez: '))
    elif adi> num:
        print('Demasiado Alto')
        adi= int(input('Ingresa un numero otra vez: '))
    else:
        break;

print('Felicidades !!!!!!!!')
