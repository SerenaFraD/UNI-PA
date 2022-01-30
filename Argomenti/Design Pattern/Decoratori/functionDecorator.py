# Scrivere il decoratore di funzione decf che fa in modo che venga 
# lanciata l ’eccezione TypeError se il numero di argomenti è diverso da 
# due. Altrimenti, se la funzione decorata restituisce un risultato, 
# questo viene aggiunto insieme al valore del primo argomento in un 
# file di nome “risultato.txt”

from functools import wraps


def decf(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if len(*args) + len(**kwargs) != 2:
            raise TypeError
        else:
            f = open("risultato.txt", "a")
            res = function(*args, **kwargs)

            if res is not None:
                f.write(res)

            if args:
                f.write(str(args[0]))
            else:
                f.write(str(next(iter(kwargs.items()))))
            
            f.write("\n")
            f.close()
    
    return wrapper
