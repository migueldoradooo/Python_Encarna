#Ejemplo 1: Numeros positivos, negativos o ceros

num = int(input("Introduce un numero: "))

if num > 0:
    print('Este numero: ', num, ' Es un numero positivo')

elif num < 0:
    print('Este numero: ', num, ' Es un numero negativo')

else:
    print('El numero es cero')



#Ejemplo 2: Contar del 1 al 10
contador = 1

for i in range(1,11):
    print(i)


#Ejemplo 3: Adivinar número

nume = 5
intro = int(input('Intenta adivinar el numero: '))


while nume != intro:
    print('fallastes')
    intro = int(input('Intenta adivinar el numero: '))

print('Adivinastes el numero')


# Ejemplo 4: Tabla de Multiplicar

num = int(input)