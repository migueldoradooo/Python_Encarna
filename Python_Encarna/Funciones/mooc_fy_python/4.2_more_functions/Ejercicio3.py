def line(num,cad):
    if len(cad) > 0:
        letra = cad[0]
    else:
        letra = "*"
    for i in range(num):
        print(letra)
    print(" ")

def square_of_hashes(num1):
    for i  in range(num1):
            line(num1,"#")
            
square_of_hashes(5)