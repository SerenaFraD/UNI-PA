import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def writeInFile():
    while True:
        oggetto = (yield)
        nome_file = (yield)
        file = open(nome_file, "a")
        file.write("{} ".format(str(oggetto)))


@coroutine
def gestore_int(ricevitore, successore):
    while True:
        oggetto = (yield)
        if isinstance(oggetto, int):
            print("Richiesta gestita da gestore_int")
            ricevitore.send(oggetto)
            ricevitore.send("file_int")
        elif successore is not None:
            successore.send(oggetto)

@coroutine
def gestore_str(ricevitore, successore):
    while True:
        oggetto = (yield)
        if isinstance(oggetto, str):
            print("Richiesta gestita da gestore_str")
            ricevitore.send(oggetto)
            ricevitore.send("file_str")
        elif successore is not None:
            successore.send(oggetto)

@coroutine
def gestoreDiDefault(successore=None):
    while True:
        oggetto = (yield)
        print("Messaggio da gestoreDiDefault: non e`stato possibile gestire la richiesta {}". format(oggetto))
        if successore is not None:
            successore.send(oggetto)

class Client:
    def __init__(self):
        self.handler = gestore_int(writeInFile(), gestore_str(writeInFile(), gestoreDiDefault(None)))

    def entrust(self, objects):
        for o in objects:
            try:
                self.handler.send(o)
            except StopIteration:
                print("La catena ha smesso di accettare richieste")

        self.handler.close()


client = Client()
parole = ["ciao", 123456, "ma non", 987654]
client.entrust(parole)
