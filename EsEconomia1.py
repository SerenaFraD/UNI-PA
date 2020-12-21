#[AUTHOR]Serena D'Urso
#[TRACCIA]Scrivere una funzione ricorsiva che si aspetta una lista di 20 numeri come argomento.
#Se la lista si compone di un solo argomento, restituisce il valore.
#Diversamente, confronta il valore della testa della lista con il valore ottenuto, dalla ricorsione, restituendo il più piccolo tra i due.
#Stampare a video il valore così ottenuto.

l = [123, 45, 1, 23, 2, 67, 54, 65, 90, 345, 234, 0, 2, 43, 98, 87, 21, 12, 37, 678]

def ricorsione(l, key, inizio = 0):
    if((len(l) - inizio) == 0):
        return key
    else:
        if(l[inizio] <= key):
            key = l[inizio]
        
    return ricorsione(l, key, inizio + 1)
    

#Chiamata della funzione: non toccare
print(ricorsione(l,123))
