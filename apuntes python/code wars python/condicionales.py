#para comparar necesito == en vez de =

v = "gut"

if v == 20:
    print("v es menos de 30")
elif v == "gut":
    print("guttentag")
else:
    print("not good")

nombre = "juan"
apellido = "blas martínez"

if nombre == "juan":
    if apellido =="blas martínez":
        print("nombre y apellido confirmados")
    else:
        print("reescriba nombre y apellido")
else:
    print("reescriba nombre y apellido")

#otros operadores lógicos
x = 3
if x > 2 or x < 3:
    print("si")
if x > 2 and x < 3:
    print("no")
if (not(x > 2 or x < 3)):
    print("meem")

if (not(v == nombre)):
    print("ded")