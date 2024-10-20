import math

numero_menor = math.inf
numero_mayor = -math.inf

for num in range(5):
    numero_nuevo = int(input("Introduzca un numero: "))
    if(numero_menor > numero_nuevo):
        numero_menor = numero_nuevo
    if(numero_mayor < numero_nuevo):
        numero_mayor = numero_nuevo

print("El numreo mayor es: " + str(numero_mayor))
print("El numero menor es: " + str(numero_menor))
