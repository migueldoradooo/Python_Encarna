#Números pares del 1 al 50

for i in range(1,51):
    if i % 2 == 0:
        print('El numero ', i , ' es par')
    elif i % 2 != 0 :
        print('El numero ', i , ' es impar')