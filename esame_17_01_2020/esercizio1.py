# da 10
import functools
import os.path
import re


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def searcher(c1: str, c2: str, receiver1: 'coroutine', receiver2: 'coroutine') -> None:
    stop1 = False
    stop2 = False

    while True:
        file_name = (yield)
        print(file_name)
        if os.path.exists(file_name):
            file = open(file_name, "r")

            testo = file.read()
            for parola in re.findall(r'\w+', testo):
                if parola[0:1] is c1:
                    try:
                        receiver1.send(parola)
                    except StopIteration:
                        stop1 = True
                elif parola[0:1] is c2:
                    try:
                        receiver2.send(parola)
                    except StopIteration:
                        stop2 = True
                if stop1 and stop2:
                    break
            file.close()
        else:
            print("Il file {} e` inesistente".format(file_name))

@coroutine
def listCreator(stop):
    lista = []

    while True:
        parola = (yield)
        lista.append(parola)
        print(lista)

        if stop == "stop":
            break


listaFile = ["file1", "file2", "file3"]
try:
    for file in listaFile:
        searcher("c", "s", listCreator("stop"), listCreator("no")).send(file)

except StopIteration:
    print("Vediamo")
