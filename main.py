from lib import *
from tabulate import tabulate

numero = int(input("¿Cuál es su número?: "))

archivo = input("¿Cuál es el nombre del archivo a procesar?: ")

datos = [
    [69, 75, 173, 34, 7, 54, 55, 185, 165, 169],
    [8, 96, 104, 37, 188, 106, 98, 156, 179, 29],
    [70, 93, 36, 147, 89, 6, 178, 15, 137, 142],
    [78, 32, 187, 168, 6, 136, 82, 123, 63, 57],
    [114, 18, 51, 172, 124, 11, 99, 2, 25, 74],
    [112, 127, 159, 88, 22, 33, 83, 44, 197, 185],
    [1, 92, 181, 9, 77, 60, 166, 128, 195, 84],
    [200, 138, 138, 5, 42, 55, 36, 139, 93, 106],
    [196, 75, 135, 132, 87, 169, 7, 134, 127, 123],
    [185, 155, 19, 110, 193, 29, 66, 109, 3, 100]
]

def imprimir_matriz(datos, numero):
    for fila in datos:
        for elemento in fila:
            if elemento == numero:
                elemento = '\033[31m{}\033[0m'.format(elemento)  # Resalta el número en rojo
            print(elemento, end='\t')
        print()

imprimir_matriz(datos, numero)


arraynum=[
    69, 75, 173, 34, 7, 54, 55, 185, 165, 169,
    8, 96, 104, 37, 188, 106, 98, 156, 179, 29,
    70, 93, 36, 147, 89, 6, 178, 15, 137, 142,
    78, 32, 187, 168, 6, 136, 82, 123, 63, 57,
    114, 18, 51, 172, 124, 11, 99, 2, 25, 74,
    112, 127, 159, 88, 22, 33, 83, 44, 197, 185,
    1, 92, 181, 9, 77, 60, 166, 128, 195, 84,
    200, 138, 138, 5, 42, 55, 36, 139, 93, 106,
    196, 75, 135, 132, 87, 169, 7, 134, 127, 123,
    185, 155, 19, 110, 193, 29, 66, 109, 3, 100
]
nodoraiz = nodo( arraynum[0] )

for i in range(1, len(arraynum), 1):
    agreganodos(nodoraiz, arraynum[i])

printArbol( nodoraiz )

inOrderArr=[]
LVR (nodoraiz, inOrderArr)
print("InOrder:", end="")
print(inOrderArr)

postOrderArr=[]
LRV (nodoraiz, postOrderArr)
print("PostOrder:", end="")
print(postOrderArr)

preOrderArr=[]
VLR (nodoraiz, preOrderArr)
print("PreOrder:", end="")
print(preOrderArr)

print("............................")

arrnodos=[
    69, 75, 173, 34, 7, 54, 55, 185, 165, 169,
    8, 96, 104, 37, 188, 106, 98, 156, 179, 29,
    70, 93, 36, 147, 89, 6, 178, 15, 137, 142,
    78, 32, 187, 168, 6, 136, 82, 123, 63, 57,
    114, 18, 51, 172, 124, 11, 99, 2, 25, 74,
    112, 127, 159, 88, 22, 33, 83, 44, 197, 185,
    1, 92, 181, 9, 77, 60, 166, 128, 195, 84,
    200, 138, 138, 5, 42, 55, 36, 139, 93, 106,
    196, 75, 135, 132, 87, 169, 7, 134, 127, 123,
    185, 155, 19, 110, 193, 29, 66, 109, 3, 100
]
nodoraiz = nodo(numero)

for i in range(len(arrnodos)):
    if i != 0:
        nodosOrdenados( nodoraiz, nodo( arrnodos[i] ) )
    
    pass



printArbol( nodoraiz )

inOrderArr=[]
LVR (nodoraiz, inOrderArr)
print("InOrder:", end="")
print(inOrderArr)


