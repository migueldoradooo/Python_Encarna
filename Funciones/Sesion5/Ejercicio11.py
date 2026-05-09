
notas = []

notas_introducidas = int(input('Introduce las notas del curso ()pon un -1 para finalizar: '))
notas.append(notas_introducidas)

def leer_notas():
    
    while True:
        notas_introducidas_leer_notas = int(input('Introduce las notas del curso ()pon un -1 para finalizar: '))
        if notas_introducidas_leer_notas != -1:
            notas.append(notas_introducidas_leer_notas)
        else:
            break
    return notas

leer_ = leer_notas()

def calcular_media():

    #Sumar todas las notas
    total_notas = len(notas)
    suma_notas = 0

    for i in range(total_notas):
        suma_notas += notas[i]
    #print(suma_notas)

    #hacer la media

    todas_notas = len(notas)
    media = suma_notas / todas_notas
    
    return media
   
media = calcular_media()

print(media)

def obtener_calificacion():
    if media < 5:
        return 'Suspenso'
    elif media > 5 and media < 7:
        return 'Aprobado'
    elif media > 7 and media < 9:
        return 'Notable'
    else:
        return 'Sobresaliente'
    
calificacion = obtener_calificacion()
def mostrar_resultados():
    print(f'Tu nota media es {media}. Y tu calificacion obtenida es {calificacion}')


mostrar_resultados()