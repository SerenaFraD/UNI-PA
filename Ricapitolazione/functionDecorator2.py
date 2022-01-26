# Scrivere il decoratore di funzione decora che trasforma la funzione 
# decorata in una funzione che lancia l’eccezione TypeError se uno o 
# più argomenti non sono di tipo str. La funzione deve restituire una 
# stringa formata dagli argomenti ricevuti in input e dal risultato 
# intervallati da uno spazio. Non dimenticate di convertire il risultato in 
# stringa quando lo inserite nella stringa output

from functools import wraps


def decora(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = str()
        lista = list(args)
        lista.extend(kwargs.values())

        for element in lista:
            if not isinstance(element, str):
                raise TypeError
            else:
                result += " " + element
        
        return str(result) + " " + str(function(*args, **kwargs))
    
    return wrapper

@decora
def funzione1(a, b, *args, **kwargs):
    return len(a) + len(b)


print(funzione1("casa", "cibo", "ciao", saluto="heeehy"))