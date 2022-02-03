from math import prod

def dFact(lista):  # la lista passata a dFact
    # vero decoratore
    def decoratore(funzione):  # funzione = g
        def wrapper(*args, **kwargs):  # argomenti del generatore
            for i in range(0, len(lista)):
                try:
                    somma = lista[i] + sum(args) + sum(kwargs.values())
                except TypeError:
                    return

                yield funzione(somma)

        return wrapper
    return decoratore


# primo test
def g(x, z=4):
    return prod([x, z])


h = dFact([0, 2, 1])(g)
t = dFact([0, 2, 1, "5", 8])(g)

print(
    "Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory")
for r in h(2):
    print(r)
print("Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi")
for r in t(2):
    print(r)


# secondo test
def g(x, z=4, *y):
    return prod([x, z] + list(y))


h = dFact([0, 2, 1])(g)
t = dFact([0, 2, 1, "5", 8])(g)
print(
    "Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory")
for r in h(2, 1, 0, 3):
    print(r)
print("Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi")
for r in t(2, 1, 0, 3):
    print(r)


# terzo test
def g(x, z=4, **y):
    return prod([x, z] + list(y.values()))


h = dFact([0, 2, 1])(g)
t = dFact([0, 2, 1, "5", 8])(g)
print("Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory")
for r in h(*(1, 2), k1=4, k2=3):
    print(r)
print("Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi")
for r in t(*(1, 2), k1=4, k2=3):
    print(r)


"""Il programma deve stampare:
Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory
8
16
12
Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi
8
16
12
Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory
0
120
24
Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi
0
120
24
Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory
24
360
120
Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi
24
360
120


"""
