# 4ª División: Función base de impresión
def line(longitud, texto):
    if texto == "":
        char = " "  
    else:
        char = texto[0]
    print(char * longitud, end="")


def print_row(spaces, stars):
    line(spaces, "")
    line(stars, "*")   
    print()              


def print_leaves(altura):
    stars = 1
    spaces = altura - 1
    for i in range(altura):
        print_row(spaces, stars)
        stars += 2
        spaces -= 1

def print_trunk(altura):

    print_row(altura - 1, 1)


def spruce(altura):
    print("¡Un abeto!")
    print_leaves(altura)
    print_trunk(altura)


spruce(3)
spruce(5)