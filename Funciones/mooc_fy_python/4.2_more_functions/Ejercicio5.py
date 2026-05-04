def spruce(n):
    print("¡un abeto!")

    for i in range(1, n + 1):
        espacios = n - i
        estrellas = 2 * i - 1
        print(" " * espacios + "*" * estrellas)
    

    print(" " * (n - 1) + "*")

spruce(5000)

