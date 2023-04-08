class Trie:
    root = None
class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False

class LinkedList:
    head = None
class Node:
    value = None
    nextNode = None
"""------------------------------------------------------------------------------------------------"""
#Ejercicio 1
"""insert(T,element)
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie) y
el valor del elemento (palabra) a agregar.
Salida: No hay salida definida"""

def add(L, element):
    addNode = Node()
    addNode.value = element
    if L.head == None:
        L.head = addNode
    else:
        addNode.nextNode = L.head
        L.head = addNode
    
def insert(T,element):
    longitud = len(element)
    position = 0
    return insertR(T,element,longitud,position)

def insertR(T,element,longitud,position):
    #Caso base
    if position == longitud:
        currentNode = T.children.head
        while currentNode != None:
            if currentNode.value.key == element[position-1]:
                currentNode.value.parent = T.children
                currentNode.value.isEndOfWord = True
                break
            currentNode = currentNode.nextNode
        return 
    #1er paso
    if T.children != None:
        currentNode = T.children.head
    else:
        T.children = LinkedList() 
        newTnode = TrieNode()
        newTnode.key = element[position]
        add(T.children, newTnode)
        currentNode = T.children.head
    #2do paso
    while currentNode != None:
        if currentNode.value.key == element[position]:
            if longitud - position > 1:
                currentNode.value.parent = T.children
                T = currentNode.value
            else:
                currentNode.value.parent = T.children
            break
        currentNode = currentNode.nextNode
    if currentNode == None:
        newTnode = TrieNode()
        newTnode.key = element[position]
        add(T.children, newTnode)
        T.children.head.value.parent = T 
        T = T.children.head.value   
    return insertR(T,element,longitud,position+1)
"""----------------------------------------------------------------"""

"""search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie) y
el valor del elemento (palabra)
Salida: Devuelve False o True según se encuentre el elemento."""

def search(T,element):
    if T.children == None:
        return False
    longitud = len(element)
    position = 0
    contadorLetras = 0
    return searchR(T,element,longitud,position,contadorLetras)

def searchR(T,element,longitud,position,contadorLetras):
    if contadorLetras == longitud:
        return True
    else:
        currentNode = T.children.head
        while currentNode != None:
            if currentNode.value.key == element[position]:
                contadorLetras += 1
                T = currentNode.value
                break
            currentNode = currentNode.nextNode 
        if currentNode == None:
            return False
        else:
            return searchR(T,element,longitud,position+1,contadorLetras)
    
                
                
                
    
    