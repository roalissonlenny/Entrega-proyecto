from .classes import *


def LVR( nodo, inOrderArr ):
    if nodo is not None:
        nodopadre = nodo
        LVR ( nodopadre.Izq, inOrderArr )
        inOrderArr.append( nodopadre.valor )
        LVR ( nodopadre.Der, inOrderArr )

    return inOrderArr

def LRV( nodo, postOrderArr ):
    if nodo is not None:
        nodopadre = nodo
        LRV ( nodopadre.Izq, postOrderArr )
        LRV ( nodopadre.Der, postOrderArr )   
        postOrderArr.append( nodopadre.valor )     
        
    return postOrderArr

def VLR( nodo, preOrderArr ):
    if nodo is not None:
        nodopadre = nodo
        preOrderArr.append( nodopadre.valor )
        VLR ( nodopadre.Izq, preOrderArr )
        VLR ( nodopadre.Der, preOrderArr )

    return preOrderArr 
    
def linkhijo( nodopadre, nodohijoIzq=None, nodohijoDer=None ):
    if nodohijoIzq is not None:
        nodopadre.Izq = nodohijoIzq

    if nodohijoDer is not None:    
        nodopadre.Der = nodohijoDer
    
    pass

#  Inicio nodosOrdenados
def nodosOrdenados( nodopadre, newnodo ):
    if newnodo.valor < nodopadre.valor: #Izquierda
        if nodopadre.Izq is None:
            nodopadre.Izq = newnodo
        else:
            nodosOrdenados(nodopadre.Izq, newnodo)

    if newnodo.valor > nodopadre.valor: #Derecha
        if nodopadre.Der is None:
            nodopadre.Der = newnodo
        else:
            nodosOrdenados(nodopadre.Der, newnodo)
pass
#  Fin nodosOrdenados

def printArbol( nodo ):
    if nodo is not None:
        nodopadre = nodo
        print( nodopadre.getArbol() )
        printArbol ( nodopadre.Izq )
        printArbol ( nodopadre.Der )

    return 0

# inicio agreganodos
def agreganodos(currentnodo, nuevonum ):
    cola=[]
    cola.append(currentnodo)

    while cola:
        currentnodo = cola.pop(0)

        if currentnodo.Izq is None:
            currentnodo.Izq = nodo( nuevonum )
            return 0

        if currentnodo.Der is None:
            currentnodo.Der = nodo( nuevonum )
            return 0

        cola.append(currentnodo.Izq)
        cola.append(currentnodo.Der)
    return 0
# fin agreganodos

