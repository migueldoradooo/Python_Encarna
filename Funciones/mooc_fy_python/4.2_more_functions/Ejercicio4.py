def line(num, string):
    return num * string

def triagle(num2):
    contador = 0
    num2 = num2+1
    
    for contador in range (num2):
        if contador <= num2:
            print(line(contador, "#"))
        contador = contador +1 




triagle(6)