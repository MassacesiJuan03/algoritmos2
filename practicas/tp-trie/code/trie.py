from linkedlist import add, length, deleteList
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
#1)
"""insert(T,element)
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie) y
el valor del elemento (palabra) a agregar.
Salida: No hay salida definida"""
    
def insert(T,element):
    longitud = len(element)
    position = 0
    listParent = LinkedList()
    return insertR(T,element.lower(),longitud,position,listParent)

def insertR(T,element,longitud,position,listParent):
    #Caso base
    if position == longitud:
        currentNode = T.children.head
        while currentNode != None:
            if currentNode.value.key == element[position-1]:
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
                if position == 0:
                    currentNode.value.parent = T
                    listParent = T.children
                    T = currentNode.value
                else:
                    currentNode.value.parent = listParent
                    listParent = T.children
                    T = currentNode.value
            else:
                currentNode.value.parent = listParent
            break
        currentNode = currentNode.nextNode
    if currentNode == None:
        newTnode = TrieNode()
        newTnode.key = element[position]
        add(T.children, newTnode)
        T.children.head.value.parent = listParent
        T = T.children.head.value   
    return insertR(T,element,longitud,position+1,listParent)
"""----------------------------------------------------------------"""
#2)
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
    LIST = LinkedList()
    TrieNODE, TrieLIST = searchR(T,element.lower(),LIST,longitud,position,contadorLetras)
    if TrieLIST != False and TrieNODE != None:
        return True
    else:
        return False

def searchR(T,element,LIST,longitud,position,contadorLetras):
    if contadorLetras == longitud:
        return T, LIST
    elif T.children == None:
        return False, False
    else:
        currentNode = T.children.head
        while currentNode != None:
            if currentNode.value.key == element[position]:
                contadorLetras += 1
                LIST = T.children
                T = currentNode.value
                break
            currentNode = currentNode.nextNode 
        if currentNode == None:
            return False, False
        else:
            return searchR(T,element,LIST,longitud,position+1,contadorLetras)
"""----------------------------------------------------------------"""
#Ejercicio 2
"""delete(T,element)
Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento."""

def delete(T, element):
    if T.children == None:
        #Caso 1 (delete)
        return False
    longitud = len(element)
    position = 0
    contadorLetras = 0
    LIST = LinkedList()
    TrieNODE, TrieLIST = searchR(T,element.lower(),LIST,longitud,position,contadorLetras)
    if TrieLIST != False and TrieNODE != False:
        position = longitud-1
        if TrieNODE.children != None:
            #Caso 3 (delete)
            if TrieNODE.isEndOfWord == False:
                return False
            else:
                TrieNODE.isEndOfWord = False
                return True
        else:
            TrieNODE.isEndOfWord = False
            return deleteR(TrieLIST,TrieNODE.parent,element,position,longitud)
    else:
        return False

def deleteR(TList,TNode,element,position,longitud):
    if position < 0:
        #Caso base
        return True
    
    if length(TList) > 1:
        #Caso 4 (delete)
        deleteList(TList,element[position])
        return True
    else:
        #Caso 2 (delete)
        deleteList(TList,element[position])
        TList = TNode
        if longitud - position != longitud:
            TNode = TNode.head.value.parent
        return deleteR(TList,TNode,element,position-1,longitud)
"""----------------------------------------------------------------"""
#Ejercicio 4
"""Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas
las palabras del árbol que empiezan por p y sean de longitud n.""" 

def autoComplete(T,p,n):
    #Nos fijamos que la lista debajo del Trie.root exista
    if T.children == None:
        return
    longitud = len(p)
    position = 0
    contadorLetras = 0
    LIST = LinkedList()
    #Buscamos el ultimo caracter de p
    TrieNODE, TrieLIST = searchR(T,p.lower(),LIST,longitud,position,contadorLetras)
    #Verificamos que exista
    if TrieNODE == False:
        return
    else:
        #Si el children es None entonces p es igual al string completo    
        if TrieNODE.children == None:
            return p
        else:
            listPy = []
            n = n - longitud
            cont = 0
            position = 0
            return autoCompleteR(TrieNODE,p,n,position,cont,listPy)
        
def autoCompleteR(Tnode,p,n,position,cont,listPy):
    #Caso base para detener la recursión
    if n == cont:
        return listPy
    
    #Lista de un Nodo
    if length(Tnode.children) == 1:
        currentNode = Tnode.children.head
        if currentNode != None:
            p = p + currentNode.value.key
            if len(listPy) > 0:
                listPy[position] = p
            else:
                listPy.insert(position,p)
        Tnode = currentNode.value
    else:
        #Lista de más de un nodo
        if Tnode.children != None:
            currentNode = Tnode.children.head
            NodeHead = Tnode.children.head.value
            #Recorrer la lista donde nos encontramos
            while currentNode != None:
                if position == 0:
                    p = p + currentNode.value.key
                    #Agregar p en una nueva posición o actualizar la posición
                    if len(listPy) > 0:
                        listPy[position] = p
                    else:
                        listPy.insert(position,p)
                    ListPy = autoCompleteR(currentNode.value,p,n,position,cont+1,listPy)
                else:
                    #Eliminar la ultima letra de la cadena si ingresamos una letra de la lista que estamos recorriendo 
                    Node = currentNode
                    if Node.value.key != NodeHead.key:
                        p = p.rstrip(p[-1]) 
                    p = p + currentNode.value.key
                    #Agregar p en una nueva posición o actualizar la posición
                    if len(listPy) - position != 0:
                        listPy[position] = p
                    else:
                        listPy.insert(position,p)
                    ListPy = autoCompleteR(currentNode.value,p,n,position,cont+1,listPy)
                position += 1
                currentNode = currentNode.nextNode
            return ListPy     
    return autoCompleteR(Tnode,p,n,position,cont+1,listPy)
"""----------------------------------------------------------------"""
#Ejercicio 5
"""Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario. Se considera que un  Trie pertenecen al mismo documento cuando:
Ambos Trie sean iguales (esto se debe cumplir)
El Trie T1 contiene un subconjunto de las palabras del Trie T2 
Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.

En otras palabras, analizar si todas las palabras de T1 se encuentran en T2."""

def T1inT2(T1,T2):
    #Ambos trie sin elementos 
    if T1.children == None and T2.children == None:
        return True
    elif T1.children == None or T2.children == None:
        return False
    else:
        lista = []
        listT1 = T1inT2R(T1.children,lista)
        listT2 = T1inT2R(T2.children,lista)
        if listT1 == listT2:
            return True
        else:
            return False
        
def T1inT2R(T,lista):
    if T == None:
        return lista
    if length(T) == 1:
        currentNode = T.head
        lista.append(currentNode.value.key)
        return T1inT2R(currentNode.value.children,lista)
    else:
        currentNode = T.head
        while currentNode != None:
            lista.append(currentNode.value.key)
            lista = T1inT2R(currentNode.value.children,lista)
            currentNode = currentNode.nextNode
        
    
    
    
    
                
            
            
    
    