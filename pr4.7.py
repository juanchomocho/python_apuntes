from random import *

numero_aleatorio = randint(0, 100)
encontrado = False

while not encontrado:
    numero_elegido = int(input("Elije un numero: "))
    if numero_aleatorio > numero_elegido:
        print("no, tu numero es demasiado pequeño")
    elif numero_aleatorio < numero_elegido:
        print("no, tu numero es demasiado grande")
    else:
        print("correcto, tu numero es " + str(numero_aleatorio))
