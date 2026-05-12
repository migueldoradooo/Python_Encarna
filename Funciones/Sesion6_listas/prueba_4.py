my_list = [1,2,3,4,5]
print(my_list)


#insertar elementos : insert , append

my_list.insert(1,8)

print(my_list)


my_list.append(10)

print(my_list)
# borrar elementos: remove , pop

my_list.remove(3) # eliminar el valor introducido entre parentesis

print(my_list)

#my_list.remove(-1) print(my_list)  elimina un valor que no existe en el array 

my_list.pop(len(my_list) -1) # elimina por posicion 

print(my_list) 