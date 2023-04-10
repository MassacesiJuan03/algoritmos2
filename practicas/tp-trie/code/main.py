from trie import insert, search, delete, autoComplete, T1inT2
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

TRIE = Trie()
T = TrieNode()
TRIE.root = T

string2 = "Mozos"
string = "Moras"
string3 = "Morza" 
#string2 = string2.rstrip(string2[-1])
#print(string2)
"""------------------------------------------------------------------------------------------------"""
#Ejercicio 1
#1)
"""insert(T,element)
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie) y
el valor del elemento (palabra) a agregar.
Salida: No hay salida definida"""
#insert(T, string)
#insert(T, string2)
#insert(T, string3)

#print(T.children.head.value.key)
#print(T.children.head.value.children.head.value.key)
#print(T.children.head.value.children.head.value.children.head.value.key)
#print(T.children.head.value.children.head.value.children.head.value.children.head.value.key)
#print(T.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.key)
#print(T.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.key)
#print(T.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.key)
#print(T.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.isEndOfWord)
"""----------------------------------------------------------------"""
#2)
"""search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie) y
el valor del elemento (palabra)
Salida: Devuelve False o True según se encuentre el elemento."""
#print(search(T,string))
#print(search(T,string2))
"""----------------------------------------------------------------"""
#Ejercicio 2
"""delete(T,element)
Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento."""
#print(delete(T,"hola"))
#print(T.children.head.value.key)
"""----------------------------------------------------------------"""
#Ejercicio 4
"""Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas
las palabras del árbol que empiezan por p y sean de longitud n.""" 
patron="Mo"
longitud = 5
#listPy = autoComplete(T,patron,longitud)
#print(listPy)
"""----------------------------------------------------------------"""
#Ejercicio 5
"""Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario. Se considera que un  Trie pertenecen al mismo documento cuando:
Ambos Trie sean iguales (esto se debe cumplir)
El Trie T1 contiene un subconjunto de las palabras del Trie T2 
Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.

En otras palabras, analizar si todas las palabras de T1 se encuentran en T2."""

TRIE1 = Trie()
T1 = TrieNode()
TRIE1.root = T1

TRIE2 = Trie()
T2 = TrieNode()
TRIE2.root = T2

cadena1 = "hola"
cadena2 = "buenas"
cadena3 = "sol"

insert(T1,cadena1)
insert(T1,cadena2)
insert(T1,cadena3)

insert(T2,cadena1)
insert(T2,cadena2)
insert(T2,cadena3)

print(T1inT2(T1,T2))
