def pedir_numero():
    num1 = int( input('Dime un numero: '  ))

    return num1 

a = pedir_numero()
b = pedir_numero()



def pedir_operacion():

    operacion = input('Ahora escribe la operacion: ')

    return operacion

op = pedir_operacion()

def calcular(a,b,op):

    if op == '+':
        resultado = a + b
    elif op == '-':
        resultado = a - b
    elif op == '/':
        resultado = a / b
        if a == 0 or b == 0:
            print('no se puede dividir entre cero')
    elif op == '*':
        resultado = a * b

    return resultado

resultado = calcular(a,b,op)

def mostrar_resultado(resultado):
    print(f'La operacion es {a} {op} {b} y su resultado es:  {resultado}')

mostrar_resultado(resultado)