notas = []

def Agregar_notas():
    
    notas_a_agregar = int(input('Dime las notas que deseas agregar: '))
    notas_a_agregar = notas_a_agregar -1 

    while len(notas) <= notas_a_agregar:
        notas_agregadas = int(input('Agrega una nota: '))
        notas.append(notas_agregadas)
    
    return notas

notas_totales = Agregar_notas()

def nota_Alta():
    nota_maxima = max(notas)

    return nota_maxima

nota_mas_alta = nota_Alta()
print(f'la nota mas alta es: {nota_mas_alta}')

def Promedio():
    
    return sum(notas) / len(notas)

media = Promedio()
print(f'La media de las notas es: {media}')

def Eliminar_nota():
    eliminada = int(input('Introduce la nota que deseas eliminar: '))

    notas.remove(eliminada)

    return(notas)

eliminados = Eliminar_nota()

print(eliminados)

