#Ejemplo 3: Adivinar número

nume = 5
intro = int(input('Intenta adivinar el numero: '))


while nume != intro:
    print('fallastes')
    intro = int(input('Intenta adivinar el numero: '))

print('Adivinastes el numero')

