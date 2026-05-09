
lista = []
numeros_lista = int(input('Cuantos numeros quieres para la lista: '))

def leer_lista():

    i = 0
    while i != numeros_lista:
        numero = int(input('pon otro numero: '))
        lista.append(numero)
        i += 1

    return lista

lista = leer_lista()

def calcular_suma(lista):
    
    return sum(lista)


def calcular_media(lista):
    return suma / numeros_lista

suma_total = calcular_suma(lista)
media_total = calcular_media(lista)


def mostrar_resultados():

    print(' ')
    print(f'La suma de la lista es de: {suma_total}')
    print(' ')
    print(f'La media de la lista es: {media_total}')


mostrar_resultados()