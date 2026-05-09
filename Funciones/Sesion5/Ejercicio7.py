
    
def pedir_nombre():
    texto = input('Introduce nombre y apellido: ')
        

    def formatear_nombre(texto_sucio):
            
        def separar_palabras(t):
            return t.split()
            
        def capitalizar(p):
            return p.capitalize()
            

        lista = separar_palabras(texto_sucio)
        lista_lista = []
        for palabra in lista:
            lista_lista.append(capitalizar(palabra))
            
        return " ".join(lista_lista)
        

    nombre_final = formatear_nombre(texto)
    return nombre_final

def mostrar_resultado(resultado):
    print(f"El nombre formateado es: {resultado}")


final = pedir_nombre()
mostrar_resultado(final)

