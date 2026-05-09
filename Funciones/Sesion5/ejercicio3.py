def pedir_edad():
    
    edad = int(input('Dime tu edad: '))

    return edad

edad = pedir_edad()

def calcular_ano(edad):
    ano_actual = 2026
    ano_nacimiento = ano_actual - edad

    return ano_nacimiento

ano = calcular_ano(edad)

def mostrar_resultado(ano):
    print(f'El año en el que nacistes es: {ano}')


mostrar_resultado(ano)