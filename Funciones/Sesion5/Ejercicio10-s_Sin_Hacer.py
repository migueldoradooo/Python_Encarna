lista_cosas = []


cosas= int(input('Dime la cantidad de productos que vas a comprar: '))
producto_inicial = int(input('Dime el precio un producto: '))

lista_cosas.append(producto_inicial)

def leer_precios():
    listado = 1
    for listado in range(cosas - 1 ):
        producto = int(input('Dime otro precio de los productos: '))
        lista_cosas.append(producto)
    #print(lista)
lista = leer_precios()

def calcular_total(lista):
    total = 0
    for i in range(cosas):
        total = total + lista[i]
    return total
    
    #print(total)
#calcular_total(lista_cosas)


total = calcular_total(lista_cosas)

def aplicar_descuentos(total):

    descuento = 25 / 100
    descontado = total * descuento
    #print(descontado)
    return descontado


ticket = aplicar_descuentos(total)


def mostrar_ticket():

    print(f'los productos con el descuento saldian a: {ticket}')

mostrar_ticket()