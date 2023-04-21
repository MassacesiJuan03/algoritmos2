import random
import string
from dictionary import insert,search,delete

#Ejercico 1 (implementación)
#1.
"""insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función
de hash (1) en el diccionario (dictionary). Resolver colisiones por
encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción
y el valor del key a insertar
Salida: Devuelve D"""
D = []
for i in range(9):
    D.append(None)
#Arreglo de [(key,value),...,(key,value)]
Array = [(1,5),(280,6),(1000,19),(4,7),(38,60),(3,74),(1111,1),(80,29)]
for i in range(len(Array)):
    D = insert(D, Array[i][0], Array[i][1])
    
#2.
"""search(D,key)
Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda
(dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key. Devuelve None si el key no se
encuentra."""
value = search(D,38)

#3.
"""delete(D,key)
Descripción: Elimina un key en la posición determinada por la función
de hash (1) del diccionario (dictionary)
Poscondición: Se debe marcar como nulo el key a eliminar.
Entrada: El diccionario sobre el se quiere realizar la eliminación y
el valor del key que se va a eliminar.
Salida: Devuelve D"""
D = delete(D,1000) 

#Ejercicio 4
"""Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: 
dado dos strings s1...sk y p1...pk, se quiere encontrar si los caracteres de p1...pk
corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.
Ejemplo 1:
Entrada: S = 'hola' , P = 'ahlo'
Salida: True, ya que P es una permutación de S
Ejemplo 2:
Entrada: S = 'hola' , P = 'ahdo'
Salida: Falso, ya que P tiene al carácter 'd'que no se encuentra en S por lo que no es una
permutación de S"""
def PpermutacionS(D,s,p):
    if len(s) != len(p):
        return False
    elif s == p:
        return False
    else:
        #Insertamos cada letra de S en el hash
        for i in range(len(s)):
            insert(D,ord(s[i]),s[i])
        #Buscamos cada letra de P en el hash
        contLetrasDeP = 0
        for i in range(len(p)):
            value = search(D,ord(p[i]))
            delete(D,ord(p[i]))
            if value != None:
                contLetrasDeP += 1
        #Verificar si P es una permutación de S
        if contLetrasDeP == len(p):
            return True 
        else:
            return False
            
s = "hola"
p = "ahlo"
D = []
for i in range(37):
    D.append(None)
Bool = PpermutacionS(D,s,p)
#Ejercicio 5
"""Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus
elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución
propuesta.
Ejemplo 1:
Entrada: L = [1,5,12,1,2]
Salida: Falso, L no tiene todos sus elementos únicos, el 1 se repite en la 1ra y 4ta posición"""
def searchRepeated(D,List):
    if List == None:
        return True
    else:
        for i in range(len(List)):
            #Se busca si el elemento se ha ingresado al hash
            value = search(D,List[i])
            if value == None:
                #En caso de no encontrarse en el hash, se inserta
                insert(D,List[i],List[i])
            else:
                #En caso de encontrar el elemento se retorna False ya que el elemento a ingresar se encuentra en el hash 
                return False
        return True
    
D = []
for i in range(37):
    D.append(None)
L = [1,5,12,4,2]
Bool = searchRepeated(D,L)

#Ejercicio 6
"""Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter
(A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que
representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e
implementar una función de hash apropiada para los códigos postales argentinos."""
def CodigoPostal(D,code):
    if code == "":
        return D
    #Calcular el código postal
    newCode = ""
    for i in code:
        if i == "c":
            #Calcular una letra aleatoria de la A-Z
            letter = str(random.choice(string.ascii_letters))
            newCode = newCode + str.upper(letter)
        elif i == "d":
            #Calcular el número aleatorio del 0-9
            number = random.randint(0,9)
            newCode = newCode + str(number)
    #Calcular la key del código postal
    #int(newCode[1:5]), newCode[inicio:final-1]
    newKey = (ord(newCode[0])*10^4) + int(newCode[1:5]) + (ord(newCode[5])*10^3) + (ord(newCode[6])*10^2) + (ord(newCode[7])*10)
    #Insertar el código en el diccionario
    D = insert(D,newKey,newCode)
    return D
    
codigo = "cddddccc"
D = []
for i in range(37):
    D.append(None)
D = CodigoPostal(D,codigo)

#Ejercicio 7
"""Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el
recuento de caracteres repetidos. Por ejemplo, la cadena 'aabcccccaaa' se convertiría en 'a2b1c5a3'.
Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su
método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras
mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta."""
def CompressionString(string):
    if string == "":
        return string 
    else:
        #Transformo las letras de la cadena a minúsculas
        string = string.lower()
        #Variables previas para calcular la cadena comprimida
        compressionString = ""
        countRep = 1
        firstLetter = string[0]
        #Calculo la cadena comprimida
        for i in range(1,len(string)):
            if string[i] == firstLetter:
                countRep += 1
            else:
                compressionString += firstLetter
                compressionString += str(countRep)
                firstLetter = string[i]
                countRep = 1
        compressionString += firstLetter
        compressionString += str(countRep)
        #Verifico que la cadena comprimida sea menor a la cadena original y la devuelvo
        #Caso contrario devuelvo la cadena original
        if len(compressionString) > len(string):
            return string
        else:
            return compressionString  
                 
cadena = "aabcccccaaa"
cadenaComprimida = CompressionString(cadena)

#Ejercicio 8
"""Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL.
Implementar esta estrategia de la forma más eficiente posible con un costo computacional
menor a O(K*L) (solución por fuerza bruta). Justificar el coste en tiempo de la solución
propuesta.
Ejemplo 1:
Entrada: A = "abracadabra" , P = "cada"
Salida: 4, índice de la primera ocurrencia de P dentro de S (abracadabra)"""      
def SearchOcurrencia(D,a1,p1):
    if a1 == "" or p1 == "":
        return 
    else:
        p1 = p1.lower()
        a1 = a1.lower()
        keyP1 = 0
        pow = len(p1) 
        for i in range(len(p1)):
            keyP1 += ord(p1[i]) * 10^(pow)
            pow -= 1        
        #Insertar la cadena a1 en un slot del diccionario
        insert(D,keyP1,p1)
        #Calcular todas las cadenas de a1 de longitud igual a p1 e insertarlas en una lista
        flag = False
        i=0
        f = len(p1)
        List = []
        while flag == False:
            if len(a1[i:f]) == len(p1):
                List.append(a1[i:f])
                i += 1
                f += 1
            else:
                flag = True 
        #Calcular el key de las cadenas de a1 de longitud igual a p1
        for i in range(len(List)):
            keyA1 = 0
            pow = len(List[i])
            for j in range(len(List[i])):
                keyA1 += ord(List[i][j]) * 10^(pow)
                pow -= 1
            #Vefificar si se encontro la ocurrencia de a1 en p1 y retornar el índice donde comienza
            stringP1 = search(D,keyA1)
            if stringP1 == p1:
                return i
        return None         
D = []
for i in range(37):
    D.append(None)            
string1 = "abracadabra"
string2 = "cada"
firstIndex = SearchOcurrencia(D,string1,string2)

#Ejercicio 9
"""Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un
algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál
es la complejidad temporal del caso promedio del algoritmo propuesto?"""
def SsubconjuntoT(D,S,T):
    if len(S) != len(T):
        return False
    #Insertar T en el hash
    for i in range(len(T)):
        insert(D,T[i],T[i]) 
    #Buscar S en el hash
    contSubconjunto = 0
    for i in range(len(S)):
        value = search(D,S[i])
        if value == S[i]:
            contSubconjunto += 1
    #Veficar que es un subconjunto de T
    if contSubconjunto == len(T):
        return True
    else:
        return False             
        
D = []
for i in range(37):
    D.append(None)               
S = [10,9,8,7,6,5]
T = [5,6,7,8,9,10]
Bool = SsubconjuntoT(D,S,T)    
