#Número mayor

numero = int(input("Introduce un número (0 para terminar): "))
mayor = numero

while numero != 0:
    if numero > mayor:
        mayor = numero
    
    numero = int(input("Introduce otro número (0 para terminar): "))

print("El número más grande es:", mayor)
