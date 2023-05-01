#Ejercicio 1
def createGraph(listV,listA):
    #Verificar que la lista de vértices no esté vacía.
    if listV == []:
        return "Incorrecto, el grafo no contiene vértices."
    else:
        #Definir la lista de adyacencia del grafo.
        listAdjacency = []
        #Recorrer los vértices del grafo.
        for i in listV:
            #Definir el diccionario que irá dentro de la lista de adyacencia del grafo.  
            dictionary = {}
            #Definir la lista de adyacencia de cada vértice del grafo.
            listAdjacencyInDictionary = []
            #Recorrer la lista de aristas del grafo.
            if listA != []:
                for j in listA:
                    #Validar el caso de ingresar aristas repetidas(con vértices ordenados o no).
                    if i == j[0]:
                        if dictionary == {}:
                            listAdjacencyInDictionary.append(j[1])
                            dictionary[i] = listAdjacencyInDictionary
                        else:
                            if j[1] not in dictionary[i]:
                                listAdjacencyInDictionary.append(j[1])
                                dictionary[i] = listAdjacencyInDictionary
                    elif i == j[1]:
                        if dictionary == {}:
                            listAdjacencyInDictionary.append(j[0])
                            dictionary[i] = listAdjacencyInDictionary
                        else:
                            if j[0] not in dictionary[i]:
                                listAdjacencyInDictionary.append(j[0])
                                dictionary[i] = listAdjacencyInDictionary
            #Si el diccionario o la listA estan vacíos es porque el vértice no tiene vértices adyacentes.
            if dictionary == {}:
                dictionary[i] = None
                listAdjacency.append(dictionary)
            else:
                listAdjacency.append(dictionary)
    return listAdjacency

#Ejercicio 2
def existPath(Graph,v1,v2):
    #Verificar que el grafo no se encuentre vacío.
    if Graph == []:
        return "El grafo está vacío."
    #Verificar que los vértices v1 y v2 pertenezcan al grafo.
    countV1 = 0
    countV2 = 0
    for i in range(len(Graph)):
        if v1 not in Graph[i]:
            countV1 += 1 
        if v2 not in Graph[i]:
            countV2 += 1
    if countV1 == len(Graph) and countV2 == len(Graph):
        return f"Los vértices {v1} y {v2} no pertenece al grafo."
    elif countV1 == len(Graph):
        return f"El vértice {v1} no pertenece al grafo."
    elif countV2 == len(Graph):
        return f"El vértice {v2} no pertenece al grafo."
    else:
        #Obtener la lista de adyacencia de v1 respecto del DFS. 
        DFSv1 = convertToDFSTree(Graph,v1)
        #Verificar que v1 no sea un vértice no conexo.
        if DFSv1 == "Vértice no conexo":
            return False
        else:
            #Verificar si existe un camino entre v1 y v2.
            for i in range(len(DFSv1)):
                    if v2 in DFSv1[i]:
                        return True
            return False

#Ejercicio 3
def isConnected(Graph):
    #Verificar que el grafo no esté vecío.
    if Graph == []:
        return "El grafo se encuentra vacío."
    else:
        #Si el grafo no esta vacío entonces calcular su DFS.
        lista = []
        lista.append(list(Graph[0].keys()))
        GraphDFS = convertToDFSTree(Graph,lista[0][0])
        if len(GraphDFS) == len(Graph):
            return True
        else:
            return False   

#Ejercicio 4
class nodeVertex:
    value = None
    parent = None
        
def isTree(Graph):
    #Verificar que el grafo no esté vacío.
    if Graph == []:
        return "El Grafo se encuentra vacio."
    #Obtener un vértice raíz del grafo.
    List = []
    ListNodeVertex = []
    for i in range(len(Graph)):
        List.append(list(Graph[i].keys()))
        #Obtener la lista de vértices de tipo nodeVertex.
        ListNode = insertVertex(List[i][0],ListNodeVertex)
    vertex = List[0][0]
    #Crear una lista para los vértices visitados.
    listVisited = []
    listVisited.append(vertex)
    #Crear una cola para colocar los vértices adyacentes no visitados.
    Queue = []
    Queue.append(vertex)
    while Queue != []:
        #Desencolar el primer elemento de la cola.
        u = Queue.pop(0)
        #Verificar que el vértice se encuentre en el grafo.
        for i in range(len(Graph)): 
            if u in Graph[i]:
                adjacencyNodes = Graph[i][u]
                break
            else:
                adjacencyNodes = None
        #Verificar que el vértice u sea conexo.
        if adjacencyNodes is not None:
            #Agregar el padre de cada vértice.
            for index in ListNode:
                if index.value in adjacencyNodes:
                    if index.parent is None:
                        index.parent = u 
            #Buscar el nodo vértice para evaluar el ciclo.
            for i in ListNode:
                if i.value == u:
                    nodeV = i
            #Recorrer la lista de adyacencia del vértice anterior(u).
            for i in adjacencyNodes:
            #Verificar que el vértice adyacente de u no se encuentre en la lista de visitados.
                if i not in listVisited:
                    Queue.append(i)
                    listVisited.append((i))
                else:
                    if nodeV.parent != i: 
                        return False
    return True              

def insertVertex(v,ListNode):
    vertexNode = nodeVertex()
    vertexNode.value = v
    ListNode.append(vertexNode)
    return ListNode

#Ejercicio 5
def isComplete(Graph):
    #Verificar que el grafo no esté vacío.
    if Graph == []:
        return "El Grafo se encuentra vacio."
    #Verificar que el grafo sea conexo.
    connectedGraph = isConnected(Graph)
    if connectedGraph is False:
        return False
    #Guardar en una lista los vértices del grafo.
    List = []
    for i in Graph:
        List.append(list(i.keys()))
    #Verificar que existe una arista para todo par de vértices.
    for i in range(len(Graph)):
        #Key del diccionario donde está el vértice.
        index = List[i][0]
        for vertex in List:
            if vertex[0] != index:
                if vertex[0] not in Graph[i][index]:
                    return False
    return True

#Ejercicio 6
def convertTree(Graph):
    #Verificar que el grafo no esté vacío.
    if Graph == []:
        return "El Grafo se encuentra vacio."
    #Verificar si el grafo ya es un árbol.
    graphTree = isTree(Graph)
    if graphTree is True:
        return "El grafo ya es un árbol."
    #Obtener un vértice raíz del grafo.
    List = []
    ListNodeVertex = []
    for i in range(len(Graph)):
        List.append(list(Graph[i].keys()))
        #Obtener la lista de vértices de tipo nodeVertex.
        ListNode = insertVertex(List[i][0],ListNodeVertex)
    vertex = List[0][0]
    #Crear una lista para los vértices visitados.
    listVisited = []
    listVisited.append(vertex)
    #Crear una cola para colocar los vértices adyacentes no visitados.
    Queue = []
    Queue.append(vertex)
    #Definir la lista donde estarán las aristas que producen ciclos.
    deleteEdges = [] 
    while Queue != []:
        #Desencolar el primer elemento de la cola.
        u = Queue.pop(0)
        #Verificar que el vértice se encuentre en el grafo.
        for i in range(len(Graph)): 
            if u in Graph[i]:
                adjacencyNodes = Graph[i][u]
                break
            else:
                adjacencyNodes = None
        #Verificar que el vértice u sea conexo.
        if adjacencyNodes is not None:
            #Agregar el padre de cada vértice.
            for index in ListNode:
                if index.value in adjacencyNodes:
                    if index.parent is None:
                        index.parent = u 
            #Buscar el nodo vértice para evaluar el ciclo.
            for i in ListNode:
                if i.value == u:
                    nodeV = i
            #Recorrer la lista de adyacencia del vértice anterior(u).
            for i in adjacencyNodes:
            #Verificar que el vértice adyacente de u no se encuentre en la lista de visitados.
                if i not in listVisited:
                    Queue.append(i)
                    listVisited.append((i))
                else:
                    if nodeV.parent != i:
                        #Agrego a la lista las aristas que hacen que el grafo no sea un árbol. 
                        deleteEdges.append((u,i))
    return deleteEdges

#Ejercicio 8
def convertToBFSTree(Graph, v):
    #Verificar que el grafo no este vacío.
    if Graph == []:
        return "El Grafo se encuentra vacio."
    #Verificar que el vértice raíz se encuentre en el grafo.        
    count = 0
    for i in range(len(Graph)):
        if v not in Graph[i]:
            count += 1
    if count == len(Graph):
        return "El Vértice raíz no se encuentra en el grafo."
    #Crear una lista para los vértices visitados.
    listVisited = []
    listVisited.append(v)
    #Crear una cola para colocar los vértices adyacentes no visitados.
    Queue = []
    Queue.append(v)
    #Definir la lista de adyacencia del BFS.
    adjacencyList = []
    #Distancia desde la raíz a cualquier vértice.
    diccDistance = {}
    distance = 0
    diccDistance[v] = distance
    while Queue != []:
        #Definir el diccionario que irá en la lista de adyacencia del BFS.
        dictionary = {}
        #Lista de adyacencia que va dentro del diccionario.
        adjacencyListInDictionary = [] 
        #Desencolar el primer elemento de la cola.
        u = Queue.pop(0)
        #Verificar que el vértice se encuentre en el grafo.
        for i in range(len(Graph)): 
            if u in Graph[i]:
                adjacencyNodes = Graph[i][u]
                break
            else:
                adjacencyNodes = None
        #Verificar que el vértice u sea conexo.
        if adjacencyNodes is not None:
            #Recorrer la lista de adyacencia del vértice anterior(u).
            for i in adjacencyNodes:
            #Verificar que el vértice adyacente de u no se encuentre en la lista de visitados.
                if i not in listVisited:
                    Queue.append(i)
                    listVisited.append((i))
                    diccDistance[i] = diccDistance[u] + 1
                    adjacencyListInDictionary.append((i,diccDistance[i]))
                    dictionary[u] = adjacencyListInDictionary
        #Agregar diccionarios vacíos a la lista del BFS (aquí se produce el ciclo).
        dictionary[u] = adjacencyListInDictionary
        adjacencyList.append(dictionary) 
    return adjacencyList

#Ejercicio 9                          
def convertToDFSTree(Graph, v):
    #Verificar que el grafo no este vacio.
    if Graph == []:
        return "El Grafo se encuentra vacio."
    #Verificar que el vértice raíz se encuentre en el grafo.        
    count = 0
    for i in range(len(Graph)):
        if v not in Graph[i]:
            count += 1
    if count == len(Graph):
        return "El Vértice raíz no se encuentra en el grafo." 
    #Crear una lista para los vértices visitados.
    listVisited = []
    listVisited.append(v)
    #Crear una cola para colocar los vértices adyacentes no visitados.
    Queue = []
    Queue.append(v)
    #Definir la lista de adyacencia del DFS.
    adjacencyList = []
    adjacencyListResult = convertToDFSTreeRecursive(Graph,v,listVisited,Queue,adjacencyList)
    return adjacencyListResult

def convertToDFSTreeRecursive(Graph,v,listVisited,Queue,adjacencyList):
    #Caso base de la recursividad.
    if Queue == []:
        return adjacencyList
    while Queue != None:
        #Definir el diccionario que irá en la lista de adyacencia del DFS.
        dictionary = {}
        #Lista de adyacencia que va dentro del diccionario.
        adjacencyListInDictionary = [] 
        #Si el grafo tiene un solo vértice.
        if len(Graph) == 1:
            dictionary[v] = adjacencyListInDictionary
            adjacencyList.append(dictionary)
            return adjacencyList
        #Verificar que el vértice se encuentre en el grafo.
        for k in range(len(Graph)): 
            if v in Graph[k]:
                adjacencyNodes = Graph[k][v]
                break
            else:
                adjacencyNodes = None
        #Caso General de la recursividad.
        if adjacencyNodes != None:
            count = 0
            for j in adjacencyNodes:
                if j in listVisited:
                    count += 1
            if count is len(adjacencyNodes):
                Queue.pop(len(Queue)-1)
                count = 0
                #Ingersar los vértices donde se producen ciclos. (linea 131-136)
                for i in adjacencyList:
                    if v not in i:
                        count += 1
                if count == len(adjacencyList):
                    dictionary[v] = adjacencyListInDictionary
                    adjacencyList.append(dictionary)
                if len(Queue) != 0:
                    comeBackQueue = convertToDFSTreeRecursive(Graph,Queue[len(Queue)-1],listVisited,Queue,adjacencyList)
                else:
                    comeBackQueue = convertToDFSTreeRecursive(Graph,Queue,listVisited,Queue,adjacencyList)
                return comeBackQueue
        else:
            return "Vértice no conexo"    
        #Verificar que el vértice u sea conexo.
        if adjacencyNodes is not None:
            #Recorrer la lista de adyacencia del vértice anterior(u).
            for i in adjacencyNodes:
            #Verificar que el vértice adyacente de u no se encuentre en la lista de visitados.
                if i not in listVisited:
                    Queue.append(i)
                    listVisited.append(i)
                    adjacencyListInDictionary.append(i)
                    dictionary[v] = adjacencyListInDictionary
                    v = i
                    break
        #No agregar diccionarios vacíos a la lista del DFS.
        if dictionary != {}:
            adjacencyList.append(dictionary)