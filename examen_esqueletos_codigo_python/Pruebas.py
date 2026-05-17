#Programa principal: calculadora simple
def main():
    numero1 = int(input('Dame un numero: '))
    numero2 = int(input('Dame otro numero: '))

    resultado_suma  = sumar(numero1,numero2)
    resultado_resta = restar(numero1,numero2)
    resultado_multiplicacion = multiplicacion(numero1,numero2)
    resultado_division = division(numero1,numero2)

    print(f'Suma es: {resultado_suma}')
    print(f'Resta es: {resultado_resta}')
    print(f'Multiplicacion es: {resultado_multiplicacion}')
    print(f'Division es: {resultado_division}')

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b
    
def multiplicacion(a,b):
    return a * b
    
def division(a,b):
    return a / b 
    

main()
