my_list_original = []
my_list_ordenada = []

numeros_lista_original = 5

numeros_introducidos = int(input('Introduce un numero (0 para finalizar): '))
my_list_original.append(numeros_introducidos)
my_list_ordenada.append(numeros_introducidos)

for i in range (numeros_lista_original):
    
    numeros = int(input('Introduce un numero: '))
    my_list_original.append(numeros)
    my_list_ordenada.append(numeros)


while numeros_introducidos != 0:
    numeros_introducidos = int(input('Introduce un numero (0 para finalizar): '))
    print(my_list_original)
    
    my_list_ordenada.append(numeros_introducidos)
    ordenados = sorted(my_list_ordenada)

    print(ordenados)
