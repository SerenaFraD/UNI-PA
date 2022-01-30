import functools

# prima versione, senza doc e __name__ settato a wrapper
def float_args_and_return(function):
    def wrapper(*args, **kwargs):
        args = [float(arg) for arg in args]
        return float(function(*args, *kwargs))

    return wrapper


# seconda versione, ora abbiamo doc, __name__ settato con il nome della funzione originale per fare traceback. CONSIGLIATO
def float_args_and_return(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        args = [float(arg) for arg in args]
        return float(function(*args, *kwargs))

    return wrapper


# Primo modo
@float_args_and_return
def mean(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)


# secondo modo
def mean(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)


mean = float_args_and_return(mean)
