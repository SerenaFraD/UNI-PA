#Scrivere una funzione ricorsiva che si aspetta una lista di 20 numeri come argomento.
#Se la lista si compone di un solo argomento, restituisce il valore.
#Diversamente, confronta il valore della testa della lista con il valore ottenuto, dalla ricorsione, restituendo il più piccolo tra i due.
#Stampare a video il valore così ottenuto.

l = [123, 45, 1, 23, 2, 67, 54, 65, 90, 345, 234, 0, 2, 43, 98, 87, 21, 12, 37, 678]

def ricorsione(l, key = l[0]):
    if(len(l) == 1):
        return l[0]
    
    result = ricorsione(l[0:len(l) - 1])
    if(result < key):
        return result
    else:
        return key


    


#Chiamata della funzione: non toccare
print(ricorsione(l))