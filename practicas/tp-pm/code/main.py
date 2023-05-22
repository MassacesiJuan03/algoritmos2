from pattern_matching import existChar, isPalindrome, mostRepeatedChar,  getBiggestIslandLen, isAnagram, verifyBalancedParentheses, reduceLen, isContained, Rabin_Karp, KMP
#Ejercicio 1
"""Implementar la función que responde a la siguiente especificación.

def existChar(String, c):
    Descripción: Confirma la existencia de un carácter específico en una cadena.
    Entrada: String con la cadena en la cual buscar el carácter, carácter a buscar en la cadena.
    Salida: Retorna True si el carácter se encuentra en la cadena, o False en caso contrario."""

#boolOutput = existChar("Hola Mundo", "a")    
#print(boolOutput)

#Ejercicio 2
"""Implementar una función que detecte si una cadena es un Palíndromo. La implementación debe responder a la siguiente especificación:

def isPalindrome(String):
    Descripción: Determina si la cadena es un palíndromo.
    Entrada: String con la cadena a evaluar.
    Salida: Retorna True si la cadena es palíndromo, o False en caso contrario."""
    
#boolOutput = isPalindrome("rapar") 
#print(boolOutput)

#Ejercicio 3    
"""Implementar la función que responde a la siguiente especificación.

def mostRepeatedChar(String):
	Descripción: Encuentra el carácter que más se repite en una cadena.
    Entrada: String con la cadena a ser evaluada.
    Salida: Retorna el carácter que más se repite. En caso que haya más de un carácter con mayor ocurrencia devuelve el primero de ellos."""

#maxCharacterRepeated = mostRepeatedChar("Te mando un beso y un abrazo")   
#print(maxCharacterRepeated)

#Ejercicio 4
"""Implementar la función que dado un String S devuelve la longitud de la isla de mayor tamaño. Una isla es una secuencia consecutiva de un mismo carácter dentro de S.
Por ejemplo S = “cdaaaaaasssbbb” su mayor isla es de tamaño 6 (aaaaaa) y además tiene dos islas de tamaño 3 (sss, bbb) el resto de las islas en s  son de tamaño 1.
def getBiggestIslandLen(String):
	Descripción: Determina el tamaño de la isla de mayor tamaño en una cadena.
    Entrada: String con la cadena a ser evaluada.
    Salida: Retorna un entero con la dimensión de la isla más grande dentro de la cadena."""        

#countIsland = getBiggestIslandLen("cdaaaaaasssbbb")
#print(countIsland)

#Ejercicio 5
"""Implementar la función que responde a la siguiente especificación.

def isAnagram(String, String):
	Descripción: Determina si una cadena es un anagrama de otra.
    Entrada: Un String con la cadena original, y otro String con el posible anagrama a evaluar.
    Salida: Retorna un True si la segunda cadena es anagrama de la primera, en caso contrario devuelve False.
    Implementar la función que responde a la siguiente especificación."""
        
#output = isAnagram("poelo", "loope")
#print(output)

#Ejercico 6
"""def verifyBalancedParentheses(String):
	Descripción: Verifica si los paréntesis contenidos en una cadena se encuentran balanceados y en orden.
    Entrada: Un String con la cadena a ser evaluada.
    Salida: Retorna un True si la cadena posee sus paréntesis correctamente balanceados, en caso contrario devuelve False.
Ejemplo: “(ccc(ccc)cc((ccc(c))))” es correcto, pero “)ccc(ccc)cc((ccc(c)))(“ no lo es, aunque tenga 
el mismo número de paréntesis abiertos que cerrados."""
                        
#verifyBalanced = verifyBalancedParentheses("ccc(ccc)cc((ccc(c))))(")    
#print(verifyBalanced)

#Ejercicio 7
"""Se tiene una cadena de caracteres y se quiere reducir a su longitud haciendo una serie de operaciones.
En cada operación se selecciona un par de caracteres adyacentes que coinciden, y se los borra.
Por ejemplo, la cadena “aab” puede ser acortada a “b” en una sola operación. 
Implementar una función que borre tantos caracteres como sea posible y devuelva la cadena resultante.

def reduceLen(String):
	Descripción: Reduce la longitud de una cadena removiendo iterativamente pares de caracteres repetidos.
    Entrada: Un String con la cadena a ser reducida.
    Salida: Retorna un String con la cadena resultante tras haber aplicado las remociones. 
Ejemplo: “aaabccddd” se puede reducir a “abd”  de la siguiente manera: 
“aaabccddd” → “abccddd” → “abddd” → “abd”"""
    
#output = reduceLen("aaabccddd") 
#print(output)

#Ejercicio 8
"""Implementar una función que dadas dos palabras determine si la segunda está contenida dentro de la primera bajo la siguiente premisa.
Una cadena s contiene la palabra “amarillo” si un subconjunto ordenado de sus caracteres deletrea la palabra amarillo.
Por ejemplo, la cadena s = "aaafffmmmarillzzzllhooo" contiene amarillo, pero s = "aaafffmmmarrrilzzzhooo" no (debido a que le falta una l).
Si ordenamos la primera cadena como s = "aaaaillllfffzzzhrmmmooo", ya no contiene la subsecuencia debido al ordenamiento.

def isContained(String,String):
	Descripción: Determina si los caracteres de una cadena se encuentran contenidos y en el mismo orden dentro de otra cadena.
    Entrada: Un String con la cadena a evaluar, y otro String con la cadena posiblemente contenida en la primera.
    Salida: Retorna un True si la segunda cadena se encuentra contenida en la primera, o False en caso contrario."""
    
#output = isContained("aaafffmmmarillzzzllhooo","amarillo")
#print(output)

#Ejercicio 13
"""Implemente el algoritmo de Rabin-Karp estudiado. 
Para el mismo deberá implementarse una función de hash que dado un patrón p de tamaño m se resuelva en O(1). 
Considerar lo detallando en las presentación del tema correspondiente a las funciones de hash en Rabin-karp."""
    
#output = Rabin_Karp("abcdf","abc")
#print(output) 

#Ejercicio 14
"""Implemente el algoritmo KMP estudiado. 	
def KMP(String,String):
	Descripción: Implementa el algoritmo KMP.
    Entrada: Un String con la cadena a evaluar, y un String con el patrón a buscar.
    Salida: Retorna un arreglo de índices con las posiciones en donde se encuentra el patrón, o None en caso de no encontrar el patrón."""   

#outputKMP = KMP("abxabcabcaby", "abcaby")
#print(outputKMP)