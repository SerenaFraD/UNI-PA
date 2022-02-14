from functools import wraps

def decora(funzione):
    @wraps(funzione)
    def wrapper(lista):
        add = 0
        for i in range(0, len(lista)):
            try:
                add += int(lista[i])
            except ValueError:
                add += 0
        return add
    return wrapper


def somma1(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


@decora
def somma(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print("Non decorata ", somma1(3.5, 6, 1.2))
print("Decorata ", somma([1.3, 4, "anna", "10"]))
