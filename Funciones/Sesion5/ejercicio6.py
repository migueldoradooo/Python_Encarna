

def pedir_texto():
    return input('Introduce el texto/frase: ')

texto = pedir_texto()

def contar_palabras(texto):

    palabras_texto = texto.split()

    return len(palabras_texto)


def contar_letras(texto):

    return len(texto)


def mostrar_resultado():
    
    print(f'{contar_palabras(texto)} palabras')

    print(f'{contar_letras(texto)} letras')

mostrar_resultado()