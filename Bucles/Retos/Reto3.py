contador_positivos = 0


for i in range(5):
    
    numero = float(input(f"Introduce el número {i + 1}: "))
    
    # Comprobamos si es positivo
    if numero > 0:
        contador_positivos += 1

print("En total, has introducido "+ {contador_positivos}+ " números positivos.")


                          