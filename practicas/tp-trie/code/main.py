from trie import insert,search
class Trie:
    root = None
class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False
    
class LinkedList:
    head = None
class Node:
    value = None
    nextNode = None

TRIE = Trie()
T = TrieNode()
TRIE.root = T

string = "Nadare"
string2 = "Jugare" 
insert(T, string)
insert(T, string2)

print(T.children.head.value.key)
print(T.children.head.value.children.head.value.key)
print(T.children.head.value.children.head.value.children.head.value.key)
print(T.children.head.value.children.head.value.children.head.value.children.head.value.key)
print(T.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.key)
print(T.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.key)
print(T.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.isEndOfWord)

print(search(T,string))
print(search(T,string2))