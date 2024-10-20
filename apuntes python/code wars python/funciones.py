#elemento que procesa datos

#print() #imprime
#dir() #funcion de los elementos
#type() #typos de elemento

def hello():
    print("hola mundo")

hello() #se deben ejecutar las funciones una vez definida

def hola(nombre):
    print("hola", nombre)

hola("Belén")
hola("Papá")
hola("Mamá")

def sim(meme="persona"):
    print("hola", meme)

sim()

#para sumar números u obtener un resultado modificado

def añadir(numero_uno, numero_dos):
    return numero_uno + numero_dos

print(añadir(8, 9))

hola = lambda numerouno, numerodos: numerouno + numerodos

print(hola(10, 12))
