from random import randint
from linkedlist import add, search, length, delete
class LinkedList:
    head = None
class Node:
    value = None
    nextNode = None

#Ejercico 1 (implementación)
#1.
"""insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función
de hash (1) en el diccionario (dictionary). Resolver colisiones por
encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción
y el valor del key a insertar
Salida: Devuelve D"""
def insert(D,key,value,list_ab):
    if len(D) == 0:
        return None,None
    #Calculamos la nueva key para asignar un nuevo slot
    position = key % len(D) 
    if D[position] == None:
        #Si el slot es Null, creamos una lista y agregamos la tupla(key,value)
        D[position] = []
        D[position].append((key,value))
    else:
        if len(D[position]) >= 3:
            """Si el len(List) >= 3 debemos buscar una nueva posición usando
            la hash_Universal-function, ya que presentamos mucho encadenamiento en un 
            solo slot"""
            D,lista_ab = universalFunctionInsert(D,key,value,list_ab)
            return D,lista_ab
        else:
            #Agregamos la tupla(key,value) a la lista en el slot dado por la hash-function
            D[position].append((key,value))
    return D,0

def universalFunctionInsert(D,key,value,list_ab):
    #Encontrar p(primo) > m
    finWhile = False
    p = len(D)+1
    while finWhile == False:
        flag = 0
        for i in range(2,p):
            if p % i == 0:
                flag = 1
        if flag == 0:
            primo = p
            finWhile = True
        else:
            p += 1   
    vuelta = 0
    Hash,lista_ab = universalFunctionInsertR(D,key,value,primo,list_ab,vuelta)
    return Hash,lista_ab
        
def universalFunctionInsertR(D,key,value,p,list_ab,vuelta):
    #LLenar listas A y B 
    A = [0]
    B = [] 
    for i in range(1,p):
        A.append(i) 
        B.append(i)
    #Buscar un valor random de A y de B
    a = randint(0,len(A))
    b = randint(1,len(B))
    #Insertar la función universal en una lista
    if vuelta == 0:
        list_ab.append((a,b))
    else:
        list_ab.pop(0)
        list_ab.append((a,b))
    #Calcular la nueva key
    position = ((a*key+b)%p) % len(D)
    if D[position] == None:
        D[position] = []
        D[position].append((key,value))
        return D,list_ab
    else:
        if len(D[position]) <= 2:
            D[position].append((key,value))
            return D,list_ab
        else:
            return universalFunctionInsert(D,key,value,p,list_ab,vuelta+1)
#2.        
"""search(D,key)
Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda
(dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key. Devuelve None si el key no se
encuentra."""
def primoMayor(D):
    #Encontrar p(primo) > m
    finWhile = False
    p = len(D)+1
    while finWhile == False:
        flag = 0
        for i in range(2,p):
            if p % i == 0:
                flag = 1
        if flag == 0:
            primo = p
            finWhile = True
        else:
            p += 1   
    return primo

def search(D,key,list_ab):
    if len(D) == 0:
        return None,None
    #Calculo la nueva key usando la hash-function
    position = key % len(D)
    if D[position] == None:
        """Si el hash en la posición que me dio la hash-function es Null es porque
        la key me la tuvo que dar la hash_Universal-function"""
        if len(list_ab) != 0:
            p = primoMayor(D)
            for i in range(len(list_ab)):
                a = list_ab[i][0]
                b = list_ab[i][1]
                position = ((a*key+b)%p) % len(D)
                if D[position] != None:
                    List = D[position]
                    break
            #Buscamos el value de la lista dentro del slot dado por la hash_Universal-function
            for i in range(len(List)):
                if List[i][0] == key:
                    return List[i][1],List 
            return None,None
        else:
            return None,None
    else:
        #Buscamos el value de la lista dentro del slot dado por la hash-function
        List = D[position]
        for i in range(len(List)):
            if List[i][0] == key:
                return List[i][1],List
        return None,None
#3.            
"""delete(D,key)
Descripción: Elimina un key en la posición determinada por la función
de hash (1) del diccionario (dictionary)
Poscondición: Se debe marcar como nulo el key a eliminar.
Entrada: El diccionario sobre el se quiere realizar la eliminación y
el valor del key que se va a eliminar.
Salida: Devuelve D"""
def delete(D,key,list_ab):
    if len(D) == 0:
        return None
    value,ListValue = search(D,key,list_ab)
    if value != None:
        for i in range(len(ListValue)):
            if ListValue[i][0] == key:
                ListValue.pop(i)
                return D
    else:
        return D
