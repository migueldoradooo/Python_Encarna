my_list = []

elementos = int(input('Ingrese los elementos que desea agregar: '))
ingresados = int(input('Ingrese un elemento que quieras agregar: '))

my_list.append(ingresados)

while len(my_list) < elementos:
    
    ingresados = int(input('Ingrese un elemento que quieras agregar: '))
    my_list.append(ingresados)

print(my_list)
