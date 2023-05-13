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
#Grafo ponderado conexo.
def isConnectedWeighted(Graph):
    #Verificar que el grafo no esté vecío.
    if Graph == []:
        return "El grafo se encuentra vacío."
    else:
        #Si el grafo no esta vacío entonces calcular su DFS.
        lista = []
        lista.append(list(Graph[0].keys()))
        GraphDFS = convertWeightedToDFSTree(Graph,lista[0][0])
        if len(GraphDFS) == len(Graph[0]):
            return True
        else:
            return False   
        
#Ejercicio 4
class nodeVertexDFS:
    value = None
    parent = None
    color = None
    distance = 0
    time = 0
        
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
    vertexNode = nodeVertexDFS()
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

#Ejercicio 7 
def countConnections(Graph):
    #Verificar que el grafo no esté vacío.
    if Graph == []:
        return "El grafo está vacío"
    #Obtener los vértices del grafo.
    listVertex = []
    for vertex in Graph:
        listVertex.append(list(vertex.keys()))
    #Definir los vértices del grafo como nodos con sus atributos.
    Lnodes = []
    for vertex in listVertex:
        listNodes = insertVertex(vertex[0], Lnodes)
    #Asignar el color a los nodos.
    for node in listNodes:
        node.color = "white"
        node.parent = None
    #Verificar la cantidad de componentes conexas.
    time = 0 
    count = 0
    listDFS = []
    for node in listNodes:
        if node.color == "white":
            listDFSResult = countConnectionsRecursive(Graph,node,time,listNodes,listDFS)
            count += 1  
    return listDFSResult, count

def countConnectionsRecursive(Graph,node,time,listNodes,listDFS):
    if node.distance == 0:
        time += 1
        node.distance = time
        node.color = "gray"
    #Obtener la lista de adyacencia de cada vértice.
    for vertex in Graph:
        if node.value in vertex:
            adjacencyNodes = vertex[node.value]
    #Verificar que la lista de adyacencia de cada nodo no esté vacía.
    if adjacencyNodes != None:
        #Buscar los vértices adyacentes de tipo nodo.
        nodeList = []
        for vertex in adjacencyNodes:
            for nodeVertex in listNodes:
                if nodeVertex.value == vertex:
                    nodeList.append(nodeVertex)
        #Recorrer la lista de nodos y realizar el DFS.
        for nodeVertex in nodeList:
            if nodeVertex.color == "white":
                nodeVertex.parent = node
                #Agregar nodos a la lista final del DFS.
                dictionary = {}
                dictionary[node.value] = nodeVertex 
                listDFS.append(dictionary)
                countConnectionsRecursive(Graph,nodeVertex,time,listNodes,listDFS)
    node.color = "black"
    time += 1
    node.time = time
    #Caso base (fin de la recursión)
    if node.parent == None:
        return listDFS
    else:
        countConnectionsRecursive(Graph,node.parent,time,listNodes,listDFS)               
    
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

#Ejercicio 10
def bestRoad(Graph,v1,v2):
    #Verificar que el grafo no esté vacío.
    if Graph == []:
        return "El grafo está vacío"
    #Verificar que los vértices v1 y v2 existen dentro del grafo.
    lista = []
    for i in range(len(Graph)):
        lista.append(list(Graph[i].keys()))
    if [v1] not in lista and [v2] not in lista:
        return f"El vértice {v1} y el vértice {v2} no se encuentran en el grafo."
    elif [v1] not in lista:
        return f"El vértice {v1} no se encuentra en el grafo."
    elif [v2] not in lista:
        return f"El vértice {v2} no se encuentra en el grafo."
    #Definir los nodos a utilizar.
    ListVertex = []
    for i in lista:
        listNodeVertex = insertVertex(i[0],ListVertex)
    #Definir el color de cada nodo.
    for node in listNodeVertex:
        node.color = "white"
        if node.value == v1:
            node.color == "gray"
    #Definir una cola.
    Queue = []
    Queue.append(v1)
    #Definir la lista de salida.
    listMinPath = []
    v2NodeVertex = nodeVertex() 
    while Queue != []:
        vertex = Queue.pop(0)
        for node in listNodeVertex:
                if node.value == vertex:
                    nodeParent = node
                    node.color = "black"
        #Obtener los vértices adyacentes de vertex.
        adjacencyList = []
        for dicc in Graph:
            if vertex in dicc:
                adjacencyList.append(dicc[vertex])
        #Verificar que el vértice tenga vértices adyacentes o sea conexo.
        if adjacencyList != []:
            for vertexADJ in listNodeVertex:
                if vertexADJ.value in adjacencyList[0]:
                    if vertexADJ.color == "white":
                        vertexADJ.color = "gray"
                        vertexADJ.parent = nodeParent
                        vertexADJ.distance = vertexADJ.parent.distance + 1
                        Queue.append(vertexADJ.value)
                        if vertexADJ.value == v2:
                            v2NodeVertex = vertexADJ
            #Agregar a la lista de salida el camino de v1 a v2.
            if v2NodeVertex.value == v2:
                while v2NodeVertex.distance != 0:
                    listMinPath.insert(0,v2NodeVertex)
                    v2NodeVertex = v2NodeVertex.parent
                listMinPath.insert(0,v2NodeVertex)
                return listMinPath
    return []                                

#Crear grafo ponderado.
def createGraphWeighted(listV,listA):
    #Verificar que la lista de vértices no esté vacía.
    if listV == []:
        return "Incorrecto, el grafo no contiene vértices."
    else:
        #Definir la lista de adyacencia del grafo.
        listAdjacency = []
        #Definir el diccionario que irá dentro de la lista de adyacencia del grafo.  
        dictionary = {}
        #Recorrer los vértices del grafo.
        for i in listV:
            #Definir la lista de adyacencia de cada vértice del grafo.
            listAdjacencyInDictionary = []
            #Recorrer la lista de aristas del grafo.
            if listA != []:
                for j in listA:
                    #Validar el caso de ingresar aristas repetidas(con vértices ordenados o no).
                    if i == j[0]:
                        listAdjacencyInDictionary.append((j[1],j[2]))
                        dictionary[i] = listAdjacencyInDictionary
                    elif i == j[1]:
                        listAdjacencyInDictionary.append((j[0],j[2]))
                        dictionary[i] = listAdjacencyInDictionary
            #Si el diccionario o la listA estan vacíos es porque el vértice no tiene vértices adyacentes.
            if listAdjacencyInDictionary == []:
                dictionary[i] = None
    listAdjacency.append(dictionary)
    return listAdjacency
#DFS para grafo ponderado.
def convertWeightedToDFSTree(Graph, v):
    #Verificar que el grafo no este vacio.
    if Graph == []:
        return "El Grafo se encuentra vacio."
    #Verificar que el vértice raíz se encuentre en el grafo.        
    if v not in Graph[0]:
        return "El Vértice raíz no se encuentra en el grafo." 
    #Crear una lista para los vértices visitados.
    listVisited = []
    listVisited.append(v)
    #Crear una cola para colocar los vértices adyacentes no visitados.
    Queue = []
    Queue.append(v)
    #Definir la lista de adyacencia del DFS.
    adjacencyList = []
    adjacencyListResult = convertWeightedToDFSTreeRecursive(Graph,v,listVisited,Queue,adjacencyList)
    return adjacencyListResult

def convertWeightedToDFSTreeRecursive(Graph,v,listVisited,Queue,adjacencyList):
    #Caso base de la recursividad.
    if Queue == []:
        return adjacencyList
    while Queue != []:
        #Definir el diccionario que irá en la lista de adyacencia del DFS.
        dictionary = {}
        #Lista de adyacencia que va dentro del diccionario.
        adjacencyListInDictionary = [] 
        #Si el grafo tiene un solo vértice.
        if len(Graph[0]) == 1:
            dictionary[v] = adjacencyListInDictionary
            adjacencyList.append(dictionary)
            return adjacencyList
        #Verificar que el vértice se encuentre en el grafo.
        if v in Graph[0]:
            adjacencyNodes = Graph[0][v]
        else:
            adjacencyNodes = None
        #Caso General de la recursividad.
        if adjacencyNodes != None:
            count = 0
            for j in adjacencyNodes:
                if j[0] in listVisited:
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
                    comeBackQueue = convertWeightedToDFSTreeRecursive(Graph,Queue[len(Queue)-1],listVisited,Queue,adjacencyList)
                else:
                    comeBackQueue = convertWeightedToDFSTreeRecursive(Graph,Queue,listVisited,Queue,adjacencyList)
                return comeBackQueue
        else:
            return "Vértice no conexo"    
        #Verificar que el vértice u sea conexo.
        if adjacencyNodes is not None:
            #Recorrer la lista de adyacencia del vértice anterior(u).
            for vertex in adjacencyNodes:
            #Verificar que el vértice adyacente de u no se encuentre en la lista de visitados.
                if vertex[0] not in listVisited:
                    Queue.append(vertex[0])
                    listVisited.append(vertex[0])
                    adjacencyListInDictionary.append(vertex[0])
                    dictionary[v] = adjacencyListInDictionary
                    v = vertex[0]
                    break
        #No agregar diccionarios vacíos a la lista del DFS.
        if dictionary != {}:
            adjacencyList.append(dictionary)

#Ejercicio 14
def PRIM(Graph):
    #Verificar que el grafo no esté vacío.
    if Graph == []:
        return "El grafo está vacío."
    #Verificar que el grafo sea conexo.
    connectedGraph = isConnectedWeighted(Graph)
    if connectedGraph == False:
        return "El grafo no es conexo."
    #Obtener los vértices del grafo.
    listaVertex = []
    listaVertex.append(list(Graph[0].keys()))
    #Crear una lista para los vértices visitados.
    listVisited = []
    listVisited.append(listaVertex[0][0])
    #Crear lista de recurrencia para saber los caminos disponibles.
    listPath = []
    listPath.append(listaVertex[0][0])
    #Definir el árbol abarcador de costo mínimo.
    treeMinimum = []
    while len(listVisited) != len(Graph[0]):
        #Definir el diccionario que irá en la lista de adyacencia.
        dictionary = {}
        #Si el grafo tiene un solo vértice.
        if len(Graph[0]) == 1:
            dictionary[v] = None
            treeMinimum.append(dictionary)
            return treeMinimum
        #Recorrer una lista para encontrar el camino más corto.
        minWeightPrevius = 99999999999
        deleteVertex = None
        for v in listPath:
            count = 0
            #Obtener la lista de adyacencia del grafo.
            if v in Graph[0]:
                adjacencyNodes = Graph[0][v]
            #Obtener el menor peso.
            for weight in adjacencyNodes:
                if weight[0] not in listVisited:
                    if weight[1] <= minWeightPrevius:
                        minWeight = weight[1]
                        minWeightPrevius = minWeight
                else:
                    count += 1
            #Eliminar vértice de la lista ya que sus aristas no se tendran más en cuenta.
            if count == len(adjacencyNodes):
                deleteVertex = v
            else:
                #Recorrer la lista de adyacencia del vértice anterior(u).
                for vertex in adjacencyNodes:
                    #Verificar que el vértice adyacente de u no se encuentre en la lista de visitados.
                    if vertex[0] not in listVisited:
                        if vertex[1] <= minWeight:
                            u = vertex[0]
                            key = v
                            minWeight = vertex[1]
        listVisited.append(u)
        listPath.append(u)
        if deleteVertex != None:
            listPath.remove(deleteVertex)
        dictionary[key] = u
        treeMinimum.append(dictionary) 
    return treeMinimum
 
#Ejercicio 21
def createGraphDijkstra(listV, listE):
    #Verificar que la lista de vértices no esté vacía.
    if listV == []:
        return "Incorrecto, el grafo no contiene vértices."
    else:
        #Definir la lista de adyacencia del grafo.
        listAdjacency = []
        #Definir el diccionario que irá dentro de la lista de adyacencia del grafo.  
        dictionary = {}
        #Recorrer los vértices del grafo.
        for i in listV:
            #Definir la lista de adyacencia de cada vértice del grafo.
            listAdjacencyInDictionary = []
            #Recorrer la lista de aristas del grafo.
            if listE != []:
                for j in listE:
                    #Validar el caso de ingresar aristas repetidas(con vértices ordenados o no).
                    if i == j[0]:
                        listAdjacencyInDictionary.append((j[1],j[2]))
                        dictionary[i] = listAdjacencyInDictionary
            #Si el diccionario o la listA estan vacíos es porque el vértice no tiene vértices adyacentes.
            if listAdjacencyInDictionary == []:
                dictionary[i] = None
    listAdjacency.append(dictionary)
    return listAdjacency

class nodeVertex:
    key = None
    value = None
    parent = None
    distance = 0
    
def shortestPath(Graph, s, v):  #Dijkstra
    if Graph == []:
        return "El grafo está vacío"
    #Verificar que los vértices v1 y v2 existen dentro del grafo.
    lista = []
    lista.append(list(Graph[0].keys()))
    if s not in lista[0] and v not in lista[0]:
        return f"El vértice {s} y el vértice {v} no se encuentran en el grafo."
    elif s not in lista[0]:
        return f"El vértice {s} no se encuentra en el grafo."
    elif v not in lista[0]:
        return f"El vértice {v} no se encuentra en el grafo."
    #Crear la lista de nodos.
    listNodes = []
    for i in range(len(lista[0])):
        listResultNodes = insertVertexDijkstra(lista[0][i], listNodes, i)
    #Init relax
    for vertexNode in listResultNodes:
        if vertexNode.value == s:
            initRelax(listResultNodes, vertexNode)
            break
    #Definir lista de nodos visitados.
    listVisited = []
    #Definir la cola.
    Queue = minQueue(listResultNodes)
    while Queue != []:
        #Obtener el vértice de la cola.
        u = Queue.pop(0)
        #Agregar el vértice a la lista de visitados.
        listVisited.append(u.value)
        #Obtener el camino de s a v.
        if u.value == v:
            #Si la distancia es la máxima es porque no existe un camino de s a v.
            if u.distance != 999999999:
                #Obtener el camino más corto de s a v.
                listShortestPath = []
                while u.parent != None:
                    listShortestPath.insert(0, u)
                    u = u.parent
                listShortestPath.insert(0, u)
                return listShortestPath
            else:
                return
        #Obtener los vértices adyacentes de u.
        adjacencyNodes = Graph[0][u.value]
        #Recorrer la lista de adyacencia de u.
        if adjacencyNodes != None:
            for vertex in adjacencyNodes:
                if vertex[0] not in listVisited:
                    relax(u,vertex, listResultNodes)
        else:
            return
        #Ordenar cola según la distancia en order ascendente
        minQueue(listResultNodes)      
    return

def insertVertexDijkstra(v,ListNode,index):
    #Definir cada vértice del grafo como un nodo con sus atributos.
    vertexNode = nodeVertex()
    vertexNode.value = v
    vertexNode.key = index
    ListNode.append(vertexNode)
    return ListNode

def relax(u, tupleV, listNodes):
    #Obtener el vértice adyacente de u en forma de nodo 
    for node in listNodes:
        if node.value == tupleV[0]:
            v = node
            break
    #Realizar relajo
    if v.distance > (u.distance + tupleV[1]):
        v.distance = u.distance + tupleV[1]
        v.parent = u    
    return

def initRelax(listNodes, v1):
    #Iniciar el relajamiento para cada vértice(nodo) del grafo.
    for node in listNodes:
        node.distance = 999999999
        node.parent = None
    v1.distance = 0
    return

def minQueue(listNodes):
    count = 0
    #Ordenar la lista de nodos en orden ascendente según su distancia (usando BubbleSort).
    while count < len(listNodes) - 1:
        for i in range(len(listNodes)-1):
            if listNodes[i].distance > listNodes[i+1].distance:
                deletedNode = listNodes.pop(i)
                listNodes.insert(i+1,deletedNode)
        count += 1
    return listNodes
