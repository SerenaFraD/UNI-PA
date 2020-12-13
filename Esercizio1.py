def copyUpTo(l, x):
    if(len(l) == 0):
        return l[:]
    else:
        if(l[len(l)-1] != x):
            return copyUpTo(l[0:len(l)-1], x) + l[len(l)-1:len(l)]
        else:
            return l[len(l):len(l)+1]
            




    
print("Hello, tutto funziona")
lista = ["c", "i", "a", "o", "s"]
print("La lista e'", lista)
print("lunghezza della lista ", len(lista))
value = "i"
lista2 = copyUpTo(lista[:], value)
print("La lista risultato e'", lista2)
print("La lista e'", lista)
