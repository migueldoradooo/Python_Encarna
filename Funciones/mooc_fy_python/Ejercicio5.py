def line(num, string):
    return num * string

def shape(anchotri,stringtri,anchorect,stringrect):
    anchotri = anchotri + 1 
    contador = 0
    
    for contador in range (anchotri):
        if contador <= anchotri:
            print(line(contador, stringtri))
        contador = contador +1 

    for contador in range(anchorect):
        print(line(anchorect,stringrect))


shape(2,"t",3,"p")




