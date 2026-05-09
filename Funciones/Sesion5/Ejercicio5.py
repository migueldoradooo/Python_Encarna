def pedir_numero_valido():
    numero_valido = 45
    def pedir_numero():
        return int(input('Introduce el numero: '))

       
    numero = pedir_numero()
    
    
    def es_valido(numero):

        while True:

            if numero != numero_valido:
                print('el numero es invalido')
                
                numero = pedir_numero()
            else:
                print(f'el numero {numero}, es correcto')
                break
                

    es_valido(numero)

pedir_numero_valido()

        

