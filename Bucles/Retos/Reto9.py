contrasena = 25
intentos = 1
usuario = int(input('Ingresa una contraseña numerica de 2 caracteres: '))


while True:
    if intentos != 3:
        if contrasena != usuario:
            intentos = intentos + 1 
            usuario = int(input('Ingresa una contraseña numerica de 2 caracteres: '))
        else:
            print('Acertastes')
            break;
    else:
        print('Cuenta Bloqueada')
        break


    












