import random

def main():
    pin_secreto = generar_pin(1000,9999)
    acceso_concedido = iniciar_contrpl(pin_secreto)
    mostrar_resultado(acceso_concedido)
    
main()

def generar_pin(minimo,maximo):
    pin = return