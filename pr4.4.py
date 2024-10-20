base = int(input("Introduce la base del triangulo: "))


for numero in range(1, (base + 1), 2):
    espacios = (base - numero) // 2
    linea = " " * espacios
    print(linea + "*" * (numero))