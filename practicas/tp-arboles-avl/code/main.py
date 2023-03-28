from avltree import rotateLeft, rotateRight, calculateBalance, reBalance
class AVLTree:
    root = None
    
class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
#"----------------------------------------------------"
Tree = AVLTree()

node0 = AVLNode()
node1 = AVLNode()
node2 = AVLNode()
node3 = AVLNode()
node4 = AVLNode()
node5 = AVLNode()

"""#Root
Tree.root = node0
node0.key = 2
node0.bf = -2
#Root right
node0.rightnode = node1
node1.key = 5
node1.bf = 1
node1.parent = node0
#Root right-right
node1.rightnode = node2
node2.key = 9
node2.bf = -1
node2.parent = node1
#Root right-left
node1.leftnode = node3
node3.key = 4
node3.bf = 0
node3.parent = node1
#Root right-right-right
node2.rightnode = node4
node4.key = 10
node4.bf = 0
node4.parent = node2
newRoot = rotateLeft(Tree,node0)"""

#Root
Tree.root = node0
node0.key = 5
#node0.bf = 0
#Root right
node0.rightnode = node1
node1.key = 6
#node1.bf = 6
node1.parent = node0
#Root left
node0.leftnode = node2
node2.key = 3
#node2.bf = 1
node2.parent = node0
#Root left-right
node2.rightnode = node3
node3.key = 4
#node3.bf = 0
node3.parent = node2
#Root left-left
node2.leftnode = node4
node4.key = 2
#node4.bf = 1
node4.parent = node2
#Root left-left-left
node4.leftnode = node5
node5.key = 1
#node5.bf = 0
node5.parent = node4

#newRoot = rotateRight(Tree,node0)
#print(newRoot)
"-----------------------------------------------"
#calculateBalance(Tree)
#print(node2.bf)
value = reBalance(Tree)
print(value)
print(Tree.root.key)
"""---------------------------------------"""

"""print(Tree.root.rightnode.key)
print(Tree.root.leftnode.key)"""