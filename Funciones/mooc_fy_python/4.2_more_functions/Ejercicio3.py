def line(num, string):
    return num * string

def square_of_hashes(num1):
    contador = 0

    while num1 > contador:
        print(line(num1,"#"))
        contador += 1 

square_of_hashes(5)