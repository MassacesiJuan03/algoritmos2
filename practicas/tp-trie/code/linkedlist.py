class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None
  
def add(L, element):
    addNode = Node()
    addNode.value = element
    if L.head == None:
        L.head = addNode
    else:
        addNode.nextNode = L.head
        L.head = addNode
        
def length(L):
    currentNode = L.head
    cont = 0
    while currentNode != None:
        cont += 1
        currentNode = currentNode.nextNode
    return cont

def deleteList(L, element):
    currentNode = L.head
    cont = 0
    antNode = currentNode
    while currentNode != None:
        if currentNode.value.key == element and currentNode.value.isEndOfWord == False and cont!=0:
            antNode.nextNode = currentNode.nextNode
            #currentNode = None
            return cont
        elif currentNode.value.key == element and currentNode.value.isEndOfWord == False and cont==0: ##
            print(currentNode.value.key)
            if antNode.nextNode == None:
                L.head = None
            else:
                L.head = antNode.nextNode
            #antNode = None
            return cont
        else:
            cont += 1
            antNode = currentNode
            currentNode = currentNode.nextNode
    return None
