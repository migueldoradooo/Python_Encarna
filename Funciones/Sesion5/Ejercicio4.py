passwd_usuario = 123456789
usuario_credencial = 'migueldoradooo._'



def pedir_usuario():
    usuario = input('Introduce tu usuario: ')

    return usuario

def pedir_password():
    passwd = int(input('Introduce la contraseña: '))

    return passwd

user = pedir_usuario()
passwd = pedir_password()

def comprobar_credenciales(user, passwd):
    if user == usuario_credencial and passwd == passwd_usuario:
        print('Acceso concedido')
    
    elif user == usuario_credencial and passwd != passwd_usuario:
        print('acceso denegado por contraseña')
    elif user != usuario_credencial and passwd == passwd_usuario:
        print('acceso denegado por usuario')

    else:
        print('no tienes acceso')




comprobar_credenciales(user, passwd)



