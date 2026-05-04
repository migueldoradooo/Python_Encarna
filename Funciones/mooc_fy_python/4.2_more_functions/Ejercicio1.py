# line(7,"%")
# line(10,"LOL")
# line(3,"")
def line(num,cad):
    if len(cad) > 0:
        letra = cad[0]
    else:
        letra = "*"
    for i in range(num):
        print(letra)
    print(" ")


line(10,"%")
line(5,"LOL")
line(4,"")