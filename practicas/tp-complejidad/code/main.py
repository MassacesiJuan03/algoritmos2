from linkedlist import insert, length
from math import trunc

class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None
"""-----------------------------------------------------------"""
#Ejercicio 5
def Contiene_Suma(A,n):
    if A is None:
        return
    else:
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i] + A[j] == n:
                    return True
    return

list = [2,6,8,3,1,0]
number = 7
output = Contiene_Suma(list,number)  
if output is True:
    print("Existe el par")
else:
    print("No existe un par")  
"""-----------------------------------------------------------"""
List = LinkedList()
insert(List, 7, 0)
insert(List, 3, 1)
insert(List, 2, 2)
insert(List, 8, 3)
insert(List, 5, 4)
insert(List, 4, 5)
insert(List, 1, 6)
insert(List, 6, 7)
insert(List, 10, 8)
insert(List, 9, 9)
def printList(L):
    currentNode = L.head
    print("[", end="")
    cont = 0 
    while currentNode != None:
        if cont == length(L)-1:
            print(currentNode.value, end="")
        else:
            print(currentNode.value, end=" ")
        cont += 1
        currentNode = currentNode.nextNode
    print("]")

print("Lista Base:")
printList(List)
print("")
"""----------------------------------------------------"""

def MergeSort(L):
    LeftList = LinkedList()
    RightList = LinkedList()
    if length(L) == 1:
        return L
    
    if length(L) > 1:
        currentNode = L.head
        long = trunc((length(L)/2))
        
        #Find the value of pivot
        auxCurrentNode = L.head
        positionPivot = 0
        if (length(L)/2) == long:
            while auxCurrentNode != None:
                if positionPivot == long-1:
                    pivot = auxCurrentNode.value
                    break
                auxCurrentNode = auxCurrentNode.nextNode
                positionPivot += 1
        else:
            while auxCurrentNode != None:
                if positionPivot == long:
                    pivot = auxCurrentNode.value
                    break
                auxCurrentNode = auxCurrentNode.nextNode
                positionPivot += 1
                
        #Find the minors to the pivot
        auxCurrentNode = L.head
        list = []
        while auxCurrentNode != None:
            if auxCurrentNode.value < pivot:
                list.append(auxCurrentNode.value)
            auxCurrentNode = auxCurrentNode.nextNode
        #print(list)

        #Add half of the minors to the left
        halfList = trunc(len(list)/2)
        for i in range(0,len(list)):
            if i < halfList:
                insert(LeftList, list[i], i)
        
        #Split the list into two list
        cont = 0
        cont2 = 0
        while currentNode != None:
            if cont < long:
                contDuplicates = 0
                for i in range(0,halfList):
                    if currentNode.value != list[i]:
                        contDuplicates += 1
                if contDuplicates == halfList:
                    insert(LeftList, currentNode.value, cont)
            else:
                insert(RightList, currentNode.value, cont2)
                cont2 += 1
            cont += 1
            currentNode = currentNode.nextNode
      
        SubListL = MergeSort(LeftList)
        SubListR = MergeSort(RightList)
        currentNodeL = SubListL.head
        currentNodeR = SubListR.head
        L.head = None
        j = 0
        while currentNodeL != None and currentNodeR != None:
            if currentNodeL.value < currentNodeR.value:
                insert(L, currentNodeL.value, j) 
                currentNodeL = currentNodeL.nextNode
            else:
                insert(L, currentNodeR.value, j)
                currentNodeR = currentNodeR.nextNode
            j += 1
        while currentNodeL == None and currentNodeR != None:
            insert(L, currentNodeR.value, j)
            j += 1
            currentNodeR = currentNodeR.nextNode
        while currentNodeR == None and currentNodeL != None:
            insert(L, currentNodeL.value, j)
            j += 1
            currentNodeL = currentNodeL.nextNode
        return L
    
ListInOrden = MergeSort(List)
print("Lista (MergeSort):")
printList(ListInOrden) 

  
    
    
        
