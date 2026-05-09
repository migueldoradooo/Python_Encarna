import random


def generar_numero():

    return random.randint(1, 50)

numero = generar_numero()

print(f'el numero oculto es este: {numero} pero no se deberia de ver')

def jugar(numero):

    def pedir_intento():

        intento = int(input('Dime un numero del 1 al 50: '))

        return intento
    intento = pedir_intento()

    def comprobar(intento, numero):
        if intento != numero:
            return False
        else: 
            return True
    
    comprobacion = comprobar(intento, numero)

    def controlar_intentos():
        intentos = 2
        
        while comprobacion == False:
            intentos -= 1
            print(f'Los intentos que te quedan son {intentos}')
            pedir_intento()
            comprobar(intento, numero)

            if intentos == 0 and numero != intento:
                print('no tienes mas intentos')

                break
        print('acertastes el numero aleatorio')

    seguridad_intentos = controlar_intentos()
    return seguridad_intentos

resultado = jugar(numero)

def mostrar_resultado():
    print(resultado)