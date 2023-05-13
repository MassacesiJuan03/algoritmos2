from graph import createGraph, convertToBFSTree, convertToDFSTree, existPath, isConnected, isTree, isComplete, convertTree, bestRoad, createGraphWeighted, isConnectedWeighted, PRIM, createGraphDijkstra, shortestPath, countConnections
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
listEdges = [(1,2),(2,5),(5,3),(3,4),(4,2),(1,5),(3,6)]
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
#deleteEdgesList = convertTree(graph)
#print(deleteEdgesList)    

#Ejercicio 7
"""Implementar la función que responde a la siguiente especificación.

def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el
grafo."""
"""DFS, numberOfComponents = countConnections(graph)
print("DFS:")
listValue = []
for dicc in DFS:
    listValue.append(list(dicc.values()))
print(listValue)
for value in listValue:
    print(value[0].value)
print(DFS)
print(numberOfComponents)"""

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
                
#Ejercicio 10
"""Implementar la función que responde a la siguiente especificación.

def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre
dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2
vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más
corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al
final a v2. En caso que no exista camino se retorna la lista vacía."""    

"""outputList = bestRoad(graph,3,1)
print(outputList)
for i in outputList:
    print("Path:",i.value)"""

#Ejercicio 14    
"""Implementar la función que responde a la siguiente especificación.

def PRIM(Grafo):
Descripción: Implementa el algoritmo de PRIM
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo"""
V = [1,2,3,4,5]
E = [(1,2,3),(1,5,1),(2,5,1),(2,4,4),(5,3,2),(4,3,1),(3,2,3)]
#graphWeighted = createGraphWeighted(V,E)
#print(graphWeighted)
#AACM = PRIM(graphWeighted)    
#print(AACM)   
#Ejercicio 15
"""Implementar la función que responde a la siguiente especificación.

def KRUSKAL(Grafo):
Descripción: Implementa el algoritmo de KRUSKAL
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo"""

"""def KRUSKAL(Graph):
    #Verificar que el grafo no esté vacío.
    if Graph == []:
        return "El grafo está vacío."
    #Verificar que el grafo sea conexo.
    connectedGraph = isConnectedWeighted(Graph)
    if connectedGraph == False:
        return "El grafo no es conexo."
    #Obtener los vértices del grafo.
    listVertex = []
    listVertex.append(list(Graph[0].keys()))
    #Crear las componentes conexas.
    listComponentConnected = []
    for vertex in listVertex[0]:
        LCC = make_set(vertex,listComponentConnected)
    #Obtener las aristas.
    listEdges = []
    for vertex in LCC:
        for edge in Graph[0][vertex]:
            edgeTypeList = list(edge)
            edgeTypeList.insert(0,vertex)
            listEdges.append(tuple(edgeTypeList))
    #Eliminar aristas repetidas
    listPositionDelete = []      
    for tupleMain in range(len(listEdges)-1):
        for tupleSecond in range(tupleMain+1,len(listEdges)):
            if listEdges[tupleMain][0] == listEdges[tupleSecond][1] and listEdges[tupleMain][1] == listEdges[tupleSecond][0]:
                listPositionDelete.append(listEdges[tupleSecond])
    for tupleMain in listPositionDelete:
        listEdges.remove(tupleMain)
    print(listEdges)
    #Ordenar las aristas de menor a mayor peso.
    SortEdgesWeight = sort_by_weight_asc(listEdges)
    print(SortEdgesWeight)
    

def make_set(vertex, LCC):
    LCC.append(vertex)
    return LCC

def sort_by_weight_asc(listEdges): #BubbleSort
    count = 0
    while count < len(listEdges) - 1:
        for i in range(len(listEdges)-1):
            if listEdges[i][2] > listEdges[i+1][2]:
                deletedEdge = listEdges.pop(i)
                listEdges.insert(i+1,deletedEdge)
        count += 1
    return listEdges"""    

#AACM = KRUSKAL(graphWeighted)
#print(E)
#print(AACM)

#Ejercicio 21
"""Implementar el Algoritmo de Dijkstra que responde a la siguiente especificación

def shortestPath(Grafo, s, v):
Descripción: Implementa el algoritmo de Dijkstra
Entrada: Grafo con la representación de Matriz de Adyacencia, vértice
de inicio s y destino v.
Salida: retorna la lista de los vértices que conforman el camino
iniciando por s y terminando en v. Devolver NONE en caso que no exista
camino entre s y v."""

"""print("Dijkstra:")
graphDirected = createGraphDijkstra(V, E)
print(graphDirected)
print("Shortest Path:")
menorCamino = shortestPath(graphDirected, 2, 1)
print(menorCamino)"""
#for node in menorCamino:
    #print(node.value, node.distance)
