class LinkedList:
    head = None
class Node:
    value = None
    nextNode = None
"""---------------------------------------------------------------------"""

def insert(L, element, position):
    insertNode = Node()
    insertNode.value = element
    currentNode = L.head
    cont = 0
    if position >= 0 and position <= length(L):
        while cont < position:
            cont += 1
            antNode = currentNode
            currentNode = currentNode.nextNode
        if position == 0:
            add(L, element)
        else:
            insertNode.nextNode = currentNode            
            antNode.nextNode = insertNode
            return position
    return None

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
