# Definire un decoratore di funzione che trasforma (una funzione che prende in input un numero
# variabile di numeri) in una funzione che prende in input una lista e opera solo sugli 
# elementi della lista di tipo float, int e str convertiti in int.

from functools import wraps


def decora(funzione):
    @wraps(funzione)
    def wrapper(lista):
       tmp = [int(lista[i]) for i in range(0, len(lista)) if isinstance(lista[i], (str, int, float))]
       return sum(tmp)
       
    return wrapper 


def somma1(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

@decora
def somma(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print("Non decorata ", somma1(3.5, 6, 1.2))
print("Decorata ", somma([1.3, 4, "6", "9"]))
