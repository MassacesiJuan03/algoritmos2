from math import trunc
from random import randint

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
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
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

"""----------------------------------------------------"""
#Ejercicio 4
def deleteByPosition(list, position, value):
    for i in range(len(list)):
        if i == position:
            list.remove(value)
            
def search(list, value, positionPivot):
    for i in range(positionPivot, len(list)):
        if list[i] == value:
            return i   
        
longitud = int(input("Ingresar la longitud de la lista: "))
list = []
for i in range(longitud):
    list.append(randint(0,10))
print(list)

listMinLeft = []
listMinRight = []

if len(list)/2 == trunc(len(list)/2):
    #LISTA DE LONGITUD PAR
    positionPivote = trunc(len(list)/2) - 1
    pivote = list[positionPivote]
    for i in range(len(list)):
        if list[i] < pivote:
            if i < positionPivote:
                listMinLeft.append(list[i])
            else:
                listMinRight.append(list[i])
else:
    #LISTA DE LONGITUD IMPAR
    positionPivote = trunc(len(list)/2)
    pivote = list[positionPivote]
    for i in range(len(list)):
        if list[i] < pivote:
            if i < positionPivote:
                listMinLeft.append(list[i])
            else:
                listMinRight.append(list[i]) 

print(listMinLeft)
print(listMinRight)
print("----------------------------")
contMaxLeft = 0
contMaxRight = positionPivote
while abs(len(listMinLeft) - len(listMinRight)) > 1:
    if len(listMinLeft) > len(listMinRight):
        if contMaxRight < len(list):
            if list[contMaxRight] >= pivote:
                MaxRight = list[contMaxRight]
                del list[contMaxRight]
                position = search(list, listMinLeft[0], 0)
                deleteByPosition(list, position, listMinLeft[0])
                list.insert(0,MaxRight)
                list.append(listMinLeft[0])
                value = listMinLeft[0]
                listMinLeft.remove(value)
                listMinRight.append(value)
        contMaxLeft += 1         
    else:
        if contMaxLeft < positionPivote:
            if list[contMaxLeft] >= pivote:
                MaxLeft = list[contMaxLeft]
                del list[contMaxLeft]
                position = search(list, listMinRight[0], positionPivote)
                deleteByPosition(list, position, listMinRight[0])
                list.append(MaxLeft)
                list.insert(0,listMinRight[0])
                value = listMinRight[0]
                listMinRight.remove(value)
                listMinLeft.append(value)
        contMaxLeft += 1 
                
print(listMinLeft)
print(listMinRight)
print(list)

   
    
    
        
