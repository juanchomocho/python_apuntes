my_str = "Good,Day"

# print(dir(my_str)) #nos dice como usarlo

#punto cambia la función de el texto

print(my_str.upper()) 
print(my_str.lower())
print(my_str.capitalize())

#reemplazar

print(my_str.replace("Good", "Bad").capitalize())

#contar si hay carcter

print(my_str.count(" "))

#comprobar si empieza o acaba con

print(my_str.startswith("Good"))
print(my_str.endswith("meem"))

#parit

print(my_str.split())
print(my_str.split(","))
print(my_str.split("o"))

#encontrar posición

print(my_str.find("d"))

#saber como de largo es el caracter

print(len(my_str))

#buscar el índice(primera posición del caracter)

print(my_str.index("G"))

#mira si es numérico o alfabético

print(my_str.isnumeric())
print(my_str.isalpha())

#determina el caracter de la posición indicada

print(my_str[4])
print(my_str[-1])

#sumar varibles y valores predeterminados

print("hoppe you have a " + my_str)

#f significa interpretar a través de python

print(f"hoppe you have a {my_str}")
print("hoppe you have a {0}".format(my_str))
