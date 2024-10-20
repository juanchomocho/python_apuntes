#funcionan las listas así

lista_1 = [1, "a", 23]
colores = ["rojo", "verde", "morado"]
good_day = list((1, "yup", "meem"))
print(type(good_day))

r = list(range(1, 6))
print(r)

print(type(colores))
print(dir(colores))

#para poner grupos de elementos enteros

# colores.append(("amarillo", "azul"))

#para poner elementos enteros

colores.extend(["amarillo", "azul"])
colores.extend(["kiwi", "manzana"])
print(colores)

#insertar en una posición

colores.insert(1, "violet")
#insertar al final
colores.insert(len(colores), "valor")
print(colores)

#quitar valores

colores.pop(0) #se basa en numero
colores.remove("verde") #se basa en nombre o tipo de dato
colores.clear() #borra todo
print(colores)

#ordenar listas

colores.sort(reverse=True)
print(colores)

#index funciona igual