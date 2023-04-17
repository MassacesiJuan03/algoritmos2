
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

def search(L, element):
    currentNode = L.head
    cont = 0
    while currentNode != None:
        if currentNode.value == element:
            return cont
        cont += 1
        currentNode = currentNode.nextNode
    return None

def delete(L, element):
    currentNode = L.head
    cont = 0
    antNode = currentNode
    while currentNode != None:
        if currentNode.value == element and cont!=0: 
            antNode.nextNode = currentNode.nextNode
            #currentNode = None
            return cont
        elif currentNode.value == element and cont==0: ##
            L.head = antNode.nextNode
            #antNode = None
            return cont
        else:
            cont += 1
            antNode = currentNode
            currentNode = currentNode.nextNode
    return None

def length(L):
    currentNode = L.head
    cont = 0
    while currentNode != None:
        cont += 1
        currentNode = currentNode.nextNode
    return cont