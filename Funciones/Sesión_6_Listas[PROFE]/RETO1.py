my_list = [1, 2, 3, 4, 5]

indice = int(input('Ingrese un indice para la lista: '))
nuevo_valor = int(input('Ingrese un nuevo valor para la lista: '))

my_list.insert(indice, nuevo_valor)

while indice != -1:
    indice = int(input('Ingrese un indice para la lista: '))
    nuevo_valor = int(input('Ingrese un nuevo valor para la lista: '))  
    
    my_list.insert(indice, nuevo_valor)

print(my_list)