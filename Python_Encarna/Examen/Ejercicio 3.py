#Calcular suma total
def suma_total():
    numero = int(input("Introduce un número: "))
    suma = 0
    while numero != 1:
        suma += numero
        numero = int(input("Introduce un número: "))
    print("La suma total es:", suma)
suma_total()