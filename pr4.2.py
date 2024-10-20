a = int(input("Pon un numero "))
b = int(input("Cuantas veces lo multiplicamos? "))

for num in range(b):
    print(str(a) + " * " + str(num + 1) + " = " + str(a*(num + 1)))