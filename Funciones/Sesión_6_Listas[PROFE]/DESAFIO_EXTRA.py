# Lista inicial de prueba con números repetidos
numeros = [23, 55, 2, 4, 6, 2, 3, 1, 2, 55]
print("Lista original:", numeros)
print("-" * 40)

# --- 1. Invertir una lista ---
lista_invertida = numeros[::-1]
print("1. Invertida:", lista_invertida)


# --- 2. Eliminar duplicados ---
sin_duplicados = []
for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)
print("2. Sin duplicados:", sin_duplicados)


# --- 3. Ordenar de mayor a menor ---
lista_ordenada = sin_duplicados.copy() 
lista_ordenada.sort(reverse=True)
print("3. Ordenada (Mayor a Menor):", lista_ordenada)


# --- 4. Encontrar el número más repetido ---
numero_mas_repetido = numeros[0]
max_repeticiones = 0

for num in numeros:
    repeticiones = numeros.count(num)
    if repeticiones > max_repeticiones:
        max_repeticiones = repeticiones
        numero_mas_repetido = num
        
print(f"4. Más repetido: El {numero_mas_repetido} (aparece {max_repeticiones} veces)")


# --- 5. Crear una lista de números pares ---
numeros_pares = []
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
        
print("5. Números pares:", numeros_pares)

