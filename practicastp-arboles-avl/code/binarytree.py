class AVLTree:
    root = None
    
class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
"""---------------------------------------------------------------"""

#Insert
def insert(B, element, key):
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key
  return insertR(B, newNode, B.root)
  
def insertR(B, newNode, currentNode):
  if B.root == None:
    B.root = newNode
    return newNode.key
  if currentNode.key != newNode.key:
    newNode.parent = currentNode
    if newNode.key > currentNode.key:
      if currentNode.rightNode == None:
        currentNode.rightNode = newNode
        return newNode.key
      else:
        insertR(B, newNode, currentNode.rightNode)
    else:
      if currentNode.leftNode == None:
        currentNode.leftNode = newNode
        return newNode.key
      else:
        insertR(B, newNode, currentNode.leftNode)
  else:
    return 
"""------------------------------------------------------------------------------"""
#Delete(key)
def deleteKey(B,key):
    if key != None:
        currentNode = recorrer_tree2(B.root, key)
        return deleteKeyR(B, currentNode, key)
    else:
        return

def deleteKeyR(B, currentNode, key):
    if currentNode == None:
        return None 
    #Delete root
    if B.root.key == key:
        if currentNode.rightNode != None:
            keyNode = B.root.key
            B.root = currentNode.rightNode
            return keyNode
        else:
            keyNode = B.root.key
            B.root = currentNode.leftNode
            return keyNode
    #Delete hoja 
    if currentNode.rightNode == None and currentNode.leftNode == None:
        if currentNode.parent.rightNode.key == key:
            keyNode = currentNode.key
            currentNode.parent.rightNode = None
            return keyNode
        else:
            keyNode = currentNode.key
            currentNode.parent.leftNode = None
            return keyNode
    #Delete una rama(con subramas y hojas)
    keyNode = buscar_menorOmayorKey(currentNode, key)
    if keyNode != None:
        return keyNode
    #Delete una rama(con al menos un hijo)
    if currentNode.parent.rightNode.key == key:
        if currentNode.rightNode != None:
            keyNode = currentNode.key
            currentNode.parent.rightNode = currentNode.rightNode
            return keyNode
        else:
            keyNode = currentNode.key
            currentNode.parent.rightNode = currentNode.leftNode
            return keyNode
    else:
        if currentNode.rightNode != None:
            keyNode = currentNode.key
            currentNode.parent.leftNode = currentNode.rightNode
            return keyNode
        else:
            keyNode = currentNode.key
            currentNode.parent.leftNode = currentNode.leftNode
            return keyNode
"""------------------------------------------------"""
#Recorrer tree2
def recorrer_tree2(currentNode, keyNode):
    if currentNode.key == keyNode:
        return currentNode
    if currentNode.key > keyNode:
        return recorrer_tree2(currentNode.leftNode, keyNode)
    else:
        return recorrer_tree2(currentNode.rightNode, keyNode)
"""------------------------------------------------"""
#Delete una rama(con subramas y hojas)        
def buscar_menorOmayorKey(currentNode, key):
    if currentNode == None:
        return
    if currentNode.rightNode.leftNode != None and currentNode.leftNode.rightNode != None:
        if currentNode.parent.rightNode.key == key:
            keyNode = currentNode.key
            currentNode.parent.rightNode = currentNode.rightNode.leftNode
            return keyNode
        else:
            keyNode = currentNode.key
            currentNode.parent.leftNode = currentNode.leftNode.rightNode
            return keyNode