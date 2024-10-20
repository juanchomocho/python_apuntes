numeros = [0, 1]

n = int(input("Cuantos numeros de la cadena de fibbonacci quieres que te muestre?: "))

for i in range(2, n):
        siguiente = numeros[i-1] + numeros[i-2]
        numeros.append(siguiente)

if n > 2:
    print(numeros)
elif n == 2:
    print("0, 1")
elif n == 1:
    print("0")
else:
    print("no puedes imprimir 0 numeros")