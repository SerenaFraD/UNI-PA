#Classe List
#Classe List -> Iterable
#List == Array

print("Lista vuota con list()") 
l = list() #restituisce lista vuota di default
print("Lista: ", l)
print("\nLista con 'ciao'")
l = list('ciao')
print("Lista: ", l)
print("\nLista con ['c', 'i', 'a', 'o']")
l = list(['c', 'i', 'a', 'o'])
print("Lista: ", l)

print("\nAppend")
l.append('s') #aggiunge un elemento alla fine
print("Lista: ", l)

print("\nExtend") 
l1 = (' Serena') 
l.extend(l1) #aggiunge alla lista tutti gli elementi di un iterable
print("Lista: ", l)

print("\nInsert")
l.insert(5, '-') #inserisce un elemento x nella posizione pos
print("Lista: ", l)

print("\nLength")
print(len(l)) #Lunghezza della lista

print("\nRemove")
l.remove('s') #rimuove la prima occorrenza di x se non presente genera errore
print("Lista: ", l)

print("\nPop")
i = l.pop(5) #rimuove l'elemento in posizione pos e lo restituisce
print("Lista: ", l, " l'elemento è ", i)
l.pop() #rimuove l'ultimo elemento
print("Lista: ", l, " l'elemento è ", i)

print("\nIndex")
i = l.index('c', 0, len(l)) #restituisce indice della prima occorrenza tra start e end
print("L'indice è ", i)

print("\nCount")
i = l.count('e') #conta il numero di occorrenze dell'elemento
print("Numero di occorrenze è ", i)

print("\nReverse")
l.reverse() #inverte la lista
print("Lista: ", l)

print("\nCopy")
l1 = l.copy() #restituisce la copia della lista
print("Copia: ", l1)

print("\nSort")
#key -> funzione con un solo argomento usato come chiave per fare il confronto
#reverse -> True per avere gli elementi in ordine decrescente
l.sort(key = None, reverse = False)
print("Lista: ", l)
l.sort(key = None, reverse = True)
print("Lista: ", l)

print("\nClear")
l.clear() #rimuove tutti gli elementi di una lista
print("Lista: ", l)
