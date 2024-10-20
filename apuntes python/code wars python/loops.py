alimentos = ["manzana", "pan", "queso", "leche"]
#print(alimentos[0])
#print(alimentos[1])
#print(alimentos[2])
#print(alimentos[3])

#una alternativa sería usar la función for que recorre todos los elementos

for alimentos in alimentos:
    if alimentos == "pan":
        break
    print(alimentos)

for números in range(1, 8):
    print(números)

contar = 4
while contar <= 10:
    print(contar)
    contar = contar + 1