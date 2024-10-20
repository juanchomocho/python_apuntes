coche = {
    "ruedas": 5, 
    "precio": 1223.21, 
    "velocidad": 120
}

persona = {
    "nombre": "dell", 
    "apellido": "couhnaguer"
}

print(type(coche))
print(dir(persona))
print(coche.keys())

del persona
#puede hacer diccionario dentro de lista

productos = [
    {"dolor": "si", "careta": "buena"}, 
    {"libro": 34, "ordenador": 5}
]
print(productos)
print(type(productos))
