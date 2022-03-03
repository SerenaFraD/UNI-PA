#  Scrivere nel file esercizio2.py una funzione applica(da_fare) che prende in input
#  una tupla da_fare che contiene tuple della forma (m, a1,a2,…) dove m è un metodo
#  di istanza di una certa classe C e a1, a2,… sono gli argomenti diversi da self con
#  cui deve essere invocato m. Nella prima tupla di da_fare, m è la classe C e gli
#  argomenti sono quelli da passare al costruttore per creare l’istanza di C su cui
#  invocare i metodi delle restanti tuple di da_fare. La funzione applica restituisce
#  una lista contenente come primo elemento l’istanza creata e come restanti elementi i
#  valori restituiti dalle invocazioni dei metodi delle restanti tuple.


# da_fare -> (m, a1, a2, ...)
# m -> method
# a1, ..., an -> args
def applica(da_fare: tuple):
    result = list()

    if callable(da_fare[0]):
        print(str(da_fare[0]))
        da_fare[0](11, 12, 14)
        pass

    return result

class C:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ciao(self, uno, dos, quattro):
        print(uno, dos, quattro)


applica((C.ciao, 10, 11, 12))
