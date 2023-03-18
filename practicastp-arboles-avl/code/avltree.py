class AVLTree:
    root = None
    
class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
"""-----------------------------------------------------------------------------"""    
def rotateLeft(Tree,avlnode):
    if avlnode != None:
        previusRoot = avlnode
        if avlnode.rightnode.rightnode != None:
            nodeRightRight = avlnode.rightnode.rightnode
        avlNewRoot = avlnode.rightnode
        if avlnode.rightnode.leftnode == None:
            """Caso Normal"""
            avlNewRoot.parent = avlNewRoot
            avlNewRoot.rightnode = nodeRightRight
            avlNewRoot.leftnode = previusRoot
        else:
            """Caso Especial"""
            nodeRightLeft = avlNewRoot.leftnode
            avlNewRoot.parent = avlNewRoot
            avlNewRoot.leftnode = previusRoot
            avlNewRoot.rightnode = nodeRightRight
            previusRoot.rightnode = nodeRightLeft    
        return avlNewRoot.key
    else:
        return 

"""-----------------------------------------------------------------------------"""    
def rotateRight(Tree,avlnode):
    if avlnode != None:
        previusRoot = avlnode
        if avlnode.leftnode.leftnode != None:
            nodeLeftLeft = avlnode.leftnode.leftnode
        avlNewRoot = avlnode.leftnode
        if avlNewRoot.rightnode == None:
            """Caso Normal"""
            avlNewRoot.parent = avlNewRoot
            avlNewRoot.leftnode = nodeLeftLeft
            avlNewRoot.rightnode = previusRoot
        else:
            """Caso Especial"""
            nodeLeftRight = avlNewRoot.rightnode
            avlNewRoot.parent = avlNewRoot
            avlNewRoot.rightnode = previusRoot
            avlNewRoot.leftnode = nodeLeftLeft
            previusRoot.leftnode = nodeLeftRight  
        return avlNewRoot.key
    else:
        return
"""-----------------------------------------------------------------------------"""
    
def calculateBalance(AVLTree):
    currentNode = AVLTree.root
    if currentNode != None:
        if currentNode.rightnode == None and currentNode.leftnode == None:
            currentNode.bf = 0
        else:
            calculateBalanceR(currentNode)
    else:
        return
    
def calculateBalanceR(currentNode):
    if currentNode == None:
        return 0
    heightLeft = calculateBalanceR(currentNode.leftnode)
    heightRight = calculateBalanceR(currentNode.rightnode)
    currentNode.bf = heightLeft - heightRight
    if heightLeft >= heightRight:
        return heightLeft + 1
    else:
        return heightRight + 1
    
"""-----------------------------------------------------------------------------"""
def reBalance(AVLTree):
    currentNode = AVLTree.root
    if currentNode != None:
        calculateBalance(AVLTree)
        if AVLTree.root.leftnode != None or AVLTree.root.rightnode != None:
            return reBalanceR(AVLTree, currentNode)
    else:
        return   
            
def reBalanceR(AVLTree, currentNode):
    if currentNode.leftnode != None:
        reBalanceR(AVLTree, currentNode.leftnode)
    if currentNode.rightnode != None:
        reBalanceR(AVLTree, currentNode.rightnode) 
        
    if currentNode.bf > 1:
        if currentNode.leftnode.bf == -1:
            rotateLeft(AVLTree, currentNode.rightnode)
            rotateRight(AVLTree, currentNode)
        else:
            rotateRight(AVLTree, currentNode)
    elif currentNode.bf < -1:
        if currentNode.rightnode.bf == 1:
            rotateRight(AVLTree, currentNode.leftnode)
            rotateLeft(AVLTree, currentNode)
        else:
            rotateLeft(AVLTree, currentNode)             
    return 
"""-----------------------------------------------------------------------------"""
#Insert
def insert(AVLTree, element, key):
    newNode = AVLNode()
    newNode.value = element
    newNode.key = key
    nodoAVL = insertR(AVLTree, newNode, AVLTree.root)
    """Recalcular los bf del AVLTree"""
    update_bf(AVLTree, nodoAVL)
    return newNode.key

def insertR(B, newNode, currentNode):
    if B.root == None:
        B.root = newNode
        return newNode.key
    if currentNode.key != newNode.key:
        newNode.parent = currentNode
    if newNode.key > currentNode.key:
        if currentNode.rightNode == None:
            currentNode.rightNode = newNode
            return newNode
        else:
            insertR(B, newNode, currentNode.rightNode)
    else:
        if currentNode.leftNode == None:
            currentNode.leftNode = newNode
            return newNode
        else:
            insertR(B, newNode, currentNode.leftNode)             
"""------------------------------------------------------------"""
def update_bf(AVLTree, nodoAVL):
    while nodoAVL != None:
        calculateBalanceR(nodoAVL)
        nodoAVL = nodoAVL.parent
    reBalance(AVLTree)  
            
"""--------------------------------------------------------------"""
#Delete(key)
def deleteKey(B,key):
    if key != None:
        currentNode = recorrer_tree2(B.root, key)
        keynode = deleteKeyR(B, currentNode, key)
        reBalance(B)
        return keynode
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
                