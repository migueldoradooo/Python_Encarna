

def line(num, cad):
    if len(cad) > 0:
        letra = cad[0]
    else:
        letra = "*"
    for i in range(num):
        print(letra)
    print(" ")

def shape(anchotri, stringtri, anchorect, stringrect):

    for contador in range(anchotri + 1):
        line(contador, stringtri)

    for contador in range(anchorect):
        line(anchorect, stringrect)


shape(2, "t", 3, "p")




