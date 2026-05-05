#Triangulo de #

def line(num,cad):
    if len(cad) > 0:
        letra = cad[0]
    else:
        letra = "*"
    for i in range(num):
        print(letra)
    print(" ")

def triagle(num2):

    for contador in range(num2 + 1):
        line(contador, "#")

triagle(8)