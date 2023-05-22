from math import trunc
def create_string_without_spaces(String):
    StringWithoutSpaces = ""
    for i in range(len(String)):
        if String[i] != " ":
            StringWithoutSpaces += String[i]
    return StringWithoutSpaces

#Ejercicio 1
def existChar(String, c):
    #Verificar que la cadena exista o no esté vacía.
    if String == "":
        return False
    #Contemplar el caso de mayúsculas y minúsculas.
    String = String.lower()
    c = c.lower()
    #Verifica si el carácter se encuentra en la cadena.
    if c in String:
        return True
    else:
        return False 

#Ejercicio 2
def isPalindrome(String):
    #Verificar que la cadena exista o no esté vacía.
    if String == "":
        return False
    #Eliminar los espacios para no tener que contarlos como un carácter.
    StringWithoutSpaces = create_string_without_spaces(String)
    #Pasar la cadena a minúsculas para contemplar si la cadena es palíndroma.
    StringWithoutSpaces = StringWithoutSpaces.lower()
    #Definir una variable indexReverse que me sirva para comparar los carácteres del final con los del principio.
    indexReverse = len(StringWithoutSpaces) - 1
    #El recorrido de la comparación depende de la longitud de la primer mitad de la cadena.
    halfLength = trunc(len(StringWithoutSpaces) / 2) - 1
    for index in range(halfLength):
        if StringWithoutSpaces[index] != StringWithoutSpaces[indexReverse]:
            return False
        else:
            indexReverse -= 1
    return True

#Ejercicio 3
def mostRepeatedChar(String):
    if String == "":
        return "Cadena de carácteres vacía."
    #Pasar la cadena a minúsculas para poder realizar la busqueda del máximo carácter repetido.
    String = String.lower()
    #Eliminar los espacios para no tener que contarlos como un carácter.
    StringWithoutSpaces = create_string_without_spaces(String)
    #Guardar el carácter más repetido y la cantidad de veces que se repite.
    #Buscar el carácter más repetido.        
    maxRepeated = StringWithoutSpaces.count(StringWithoutSpaces[0])
    maxRepeatedChar = StringWithoutSpaces[0]
    for char in StringWithoutSpaces:
        if StringWithoutSpaces.count(char) > maxRepeated:
            maxRepeated = StringWithoutSpaces.count(char)
            maxRepeatedChar = char
    return maxRepeatedChar

#Ejercicio 4
def getBiggestIslandLen(String):
    if String == "":
        return "La cadena está vacía."
    #Pasar la cadena a minúsculas para poder realizar la busqueda del máximo carácter repetido.
    String = String.lower()
    #Eliminar los espacios para no tener que contarlos como un carácter.
    StringWithoutSpaces = create_string_without_spaces(String)
    previusChar = StringWithoutSpaces[0]
    countMax =  1
    previusCountIsland = 1
    for index in range(1,len(StringWithoutSpaces)):
        if previusChar == StringWithoutSpaces[index]:
            countMax += 1
            if countMax > previusCountIsland:
                previusCountIsland = countMax
        else:
            countMax = 1
            previusChar = StringWithoutSpaces[index]
    return previusCountIsland

#Ejercicio 5
def isAnagram(stringOriginal,stringAnagram):
    # n = len(stringAnagram)
    # m = len(stringOriginal)
    #Si alguna está vacía retornar.
    if stringOriginal == "" or stringAnagram == "":
        return
    #Ambas deben ser de igual longitud.
    elif len(stringAnagram) != len(stringOriginal):
        return False
    #Tener todo en minúsculas para no hacer excepciones.
    stringOriginal = stringOriginal.lower()
    stringAnagram = stringAnagram.lower()
    #Crear el hash para insertar el anagrama carácter a carácter.
    hash = []
    createHash(hash, stringAnagram)
    #Insertar los carácteres del anagrama al hash.
    for char in stringAnagram:
        insertHash(hash,char)
    #Buscar carácter a carácter en el hash.
    for char in stringOriginal:
        findChar = searchHash(hash,char)
        if findChar == False:
            return False
    return True
        
def createHash(D,Anagram):
    #Se dio una longitud cualquiera al hash.
    for i in range(len(Anagram)+30):
        D.append(None)
    return

def insertHash(hash,character):
    keyHash = ord(character) % len(hash)
    if hash[keyHash] == None:
        listValues = []
        listValues.append(character)
        hash[keyHash] = listValues
    else:
        hash[keyHash].append(character)
    return

def searchHash(hash,character):
    keyHash = ord(character) % len(hash)
    if hash[keyHash] != None:
        for i in range(len(hash[keyHash])):
            if hash[keyHash][i] == character:
                hash[keyHash].pop(i)
                if hash[keyHash] == []:
                    hash[keyHash] = None
                return True
    return False

#Ejercicio 6
def verifyBalancedParentheses(String):
    #Verificar que la cadena no esté vacía.
    if String == "":
        return "La cadena está vacía."
    #Crear una lista solo con los paréntesis.
    listParentheses = []
    for char in String:
        if char == "(" or char == ")":
            listParentheses.append(char)
    #Calcular el balanceo de paréntesis mediante la eliminación de paréntesis balanceados.
    listOpenParentheses = []    
    for char in listParentheses:
        if char == ")" and listOpenParentheses == []:
            return False 
        elif char == "(":
            listOpenParentheses.append(char)
        elif char == ")":
            listOpenParentheses.pop(0)
    #Si la lista de paréntesis abiertos es nula es porque se balancearon todos los paréntesis.
    if listOpenParentheses == []:
        return True
    else:
        return False
    
#Ejercicio 7
def reduceLen(String):
    if String == "":
        return
    if len(String) == 1:
        return String
    String = String.lower()
    newString = ""
    for i in range(0, len(String), 2):
        if i != len(String)-1:
            if String[i] != String[i + 1]:
                newString += String[i] + String[i + 1]
            if (i + 1) == (len(String) - 2):
                newString += String[i + 2]
    return newString

#Ejercicio 8
def isContained(string, pattern):
    #Verificar que ninguna cadena se encuentre vacía.
    if string == "" or pattern == "":
        return
    #Trabajar solo con carácteres en minúscula.
    string = string.lower()
    pattern = pattern.lower()
    #Crear el hash donde luego se consultara.
    hash = []
    createHash(hash,pattern)
    #Ingresar carácter a carácter en el hash.
    for char in pattern:
        insertHashWithoutRepeated(hash,char)    
    index = 0
    newString = ""
    for char in string:
        #Si son iguales agregamos el carácter a la nueva cadena.
        if char == pattern[index]:
            newString += char
            index += 1
        else:
            #Si son distintos verificar que el carácter esté en el hash para saber si el carácter no está en el orden correcto.
            #Si esto sucede se retorna falso ya que no cumple con que los carácteres del patrón se vayan encontrando en el orden adecuado.
            if searchInHash(hash,char) == True:
                if newString[len(newString)-1] != char:
                    return False
        #Se confirma que el patrón existe en la cadena.
        if len(newString) == len(pattern):
            return True
    return False

def insertHashWithoutRepeated(hash,character):
    hashKey = (ord(character)*pow(10,ord(character))) % len(hash)
    if hash[hashKey] == None:
        hash[hashKey] = character
    return

def searchInHash(hash,character):
    keyHash = (ord(character)*pow(10,ord(character))) % len(hash)
    if hash[keyHash] != None:
        for i in range(len(hash[keyHash])):
            if hash[keyHash][i] == character:
                return True
    return False

#Ejercicio 13
def Rabin_Karp(String, Pattern):
    if String == "" or Pattern == "":
        return
    #Se calcula el hash-key del patrón.
    hashkeyPattern = hash_function(Pattern)
    #print(hashkeyPattern)
    n =  len(String)
    m = len(Pattern)
    for s in range(0,n-m+1):
        #Se busca una subcadena de la cadena mayor de tamaño igual al patrón.
        subString = subStr(String, s, s+m)  
        #Si son iguales los hash-key, entonces hay que verificar si las posibles cadenas son iguales.
        if hash_function(subString) == hashkeyPattern:
            if subString == Pattern:
                return True
    return False
                        
def hash_function(pattern):
    keyFunction = 0
    i = len(pattern) - 1 
    for char in pattern:
        keyFunction += (pow(128,i) * ord(char))
        i -= 1
    return keyFunction
    
def subStr(String,start,final):
    subString = String[start:final]
    return subString

#Ejercicio 14
def KMP(T, P):
    #Verificar que ninguna cadena se encuentre vacía.
    if T == "" or P == "": 
        return
    #Crear el array del patrón con el máximo prefijo y sus valores.
    pi = max_prefix(P)
    index = 0
    for j in range(len(T)):
        if T[j] != P[index]:
            char, prefixIndex = transition_function(pi, index)
            #Si se cumple la condición el index empezara desde el índice siguiente del sufijo correspondiente ya calculado. 
            if char == T[j]:
                index = prefixIndex
            #Si no se cumple es porque el carácter siguiente del sufijo de P es distinto de T[j](se pierde la secuencia del patrón y se vuelve a empezar).
            else:
                index = 0
        else:
            index += 1
        #Se encontro el patrón en la cadena.
        if index == len(P)-1:
            return pi
    return None

def transition_function(pi, index):
    tuplePrefix = pi[index - 1]
    valuePrefix = tuplePrefix[0]
    qTuple = pi[valuePrefix]
    character = qTuple[1]
    return character, valuePrefix

def max_prefix(P):
    #Index para la comparación.
    j = 0
    #Creamos la lista donde se cuenta cual es el mayor prefijo que a su vez es sufijo de P.
    arrayPrefix = []
    arrayPrefix.insert(0,(0,P[j]))
    for i in range(1,len(P)):
        #Si los carácteres son distintos es porque se rompe la secuencia del prefijo, entonces
        #se vuelve al P[j-1](value) y de ahí se compara con el elemento que se encuentra en P[j-1],
        #si es igual el prefijo es de longitud 1 y si no es igual es 0.
        if P[j] != P[i]:
            if arrayPrefix[j-1][0] != 0:
                index = arrayPrefix[j-1][0] - 1
            else:
                index = arrayPrefix[j-1][0]
            if arrayPrefix[index][1] == P[i]:
                arrayPrefix.insert(i,(1,P[i]))
            else:
                arrayPrefix.insert(i,(0,P[i]))
        #Si son iguales solo se agrega a la lista ya que se encontro un prefijo y se actualiza j para seguir comparando.
        else:
            arrayPrefix.insert(i,(j+1,P[i]))
            j += 1        
    return arrayPrefix