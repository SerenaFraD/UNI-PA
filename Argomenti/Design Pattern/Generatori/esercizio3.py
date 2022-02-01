# Scrivere nel file esercizio1.py una funzione generatrice generatore(L,X) che prende in
# input una lista L di numeri e una lista di interi X. Indichiamo con Li l’i-esimo
# elemento di L e con Xi è l’i-esimo elemento di X (ovvero gli elementi di indice i-1 delle
# due liste rispettivamente). La funzione deve restituire un iteratore per il quale l’i-esima
# invocazione di next (con i<=lunghezza(X)), si comporta come segue:
# • se 0 <= xi < lunghezza(L), next restituisce il valore ottenuto sommando i primi xi valori di Li
# • se xi <0 oppure xi >=lunghezza(L), next restituisce l’eccezione IndexError.

# L -> lista numeri
# X -> lista interi
def generatore(L, X):
    for i in range(0, len(X)):
        if X[i] < 0 or X[i] >= len(L):
            yield IndexError('Fuori dagli indici')
        else:
            yield sum(L[0:X[i]])


try:
    for x in generatore([1, 2, 3, 4, 5, 6], [8, 3, 4, 5]):
        print(x)
except IndexError as e:
    print(e)
