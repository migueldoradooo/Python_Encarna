def getLetter(cadena):
    if len(cadena)>0:
        letra = cadena[0]
    else:
        letra = '*'
    return letra


def print_line(letter, numero):
    for i in range(numero):
        print(letter, end="")

    print()















def line(numero,cadena):
    
    
    letter = getLetter(cadena)

    print_line(letter, numero)
def box_of_hashes(num1):
    for i  in range(num1):
        line(10,"#")
box_of_hashes(5)

