from graph import createGraph, convertToBFSTree, convertToDFSTree, existPath, isConnected, isTree, isComplete, convertTree
#Ejercicio 1
"""Implementar la función crear grafo que dada una lista de vértices y una lista de aristas cree un grafo
con la representación por Lista de Adyacencia.

def createGraph(List, List)
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista
de aristas donde por cada par de elementos representa una conexión
entre dos vértices.
Salida: retorna el nuevo grafo"""
listVertex = [1,2,3,4,5,6]
listEdges = [(1,2),(2,5),(5,3),(3,4),(4,2),(1,5)]
"""for i in range(len(listVertex)-1):
    for j in range(i+1,len(listVertex)):
        listEdges.append((listVertex[i],listVertex[j]))"""    
graph = createGraph(listVertex,listEdges)
print("Grafo:")
print(graph)

#Ejercicio 2
"""Implementar la función que responde a la siguiente especificación.

def existPath(Grafo, v1, v2):
Descripción: Implementa la operación existe camino que busca si existe
un camino entre los vértices v1 y v2
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2
vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso
contrario."""        
"""listVertex = [1,2,3,4,5,6]
print("Exist path:")
for i in listVertex:
    for j in listVertex:
        if i != j:
            boolPath = existPath(graph,i,j)
            print(f"¿Existe un camino entre {i} y {j} ?")
            print(boolPath)"""

#Ejercicio 3
"""Implementar la función que responde a la siguiente especificación.

def isConnected(Grafo):
Descripción: Implementa la operación es conexo
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices,
False en caso contrario."""        
"""GrafoConexo = isConnected(graph)
print(GrafoConexo)"""

#Ejercicio 4
"""Implementar la función que responde a la siguiente especificación.

def isTree(Grafo):
Descripción: Implementa la operación es árbol
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol."""
#boolIsTree = isTree(graph)
#print(boolIsTree)

#Ejercicio 5
"""Implementar la función que responde a la siguiente especificación.

def isComplete(Grafo):
Descripción: Implementa la operación es completo
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo."""
"""boolIsComplete = isComplete(graph)
print(boolIsComplete)"""

#Ejercicio 6
"""Implementar una función que dado un grafo devuelva una lista de aristas que si se eliminan el grafo
se convierte en un árbol. Respetar la siguiente especificación.

def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo
resultante se convierte en un árbol."""        
deleteEdgesList = convertTree(graph)
print(deleteEdgesList)    
    

#Ejercicio 8
"""Implementar la función que responde a la siguiente especificación.

def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice
que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del
grafo recibido usando v como raíz.""" 
#Otra manera de obtener las keys de un diccionario.
"""lista = []
for i in range(len(graph)):
    lista.append(list(graph[i].keys()))
    GraphBFS = convertToBFSTree(graph,lista[i][0])
    print("Lista de adyacencia del BFS, vértice raíz:",lista[i][0])
    print(GraphBFS)"""      

#listVertex = [1,2,3,4,5,6]
#print("Recorrido BFS:")
#for i in listVertex:
"""GraphBFS = convertToBFSTree(graph,1)
print("Lista de adyacencia del BFS, vértice raíz:",1)
print(GraphBFS) 
print("")"""

#Ejercicio 9         
"""Implementar la función que responde a la siguiente especificación.

def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice
que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del
grafo recibido usando v como raíz."""           
"""listVertex = [1,2,3,4,5,6]
print("Recorrido DFS:")
for i in listVertex:
    GraphDFS = convertToDFSTree(graph,i)
    print("Lista de adyacencia del DFS, vértice raíz:",i)
    print(GraphDFS)"""    
                
    
