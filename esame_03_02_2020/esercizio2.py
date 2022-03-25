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
def gestore_tuple(successore):
    while True:
        oggetto = (yield)
        if isinstance(oggetto, tuple):
            if isinstance(oggetto[0], IDoNothing):
                idn = IDoNothing(oggetto[1:])
                print("Richiesta gestita da gestore_tuple: e` stata creata un’istanza della classe {} con i seguenti attributi {}".format(idn, idn.__dict__))
            else:
                print("Richiesta gestita da gestore_tuple: istanza non creata perche’ il primo elemento della tupla non e` una classe definita nel modulo esercizio2.py")
            #ricevitore.send(oggetto)
            #ricevitore.send("file_str")
        elif successore is not None:
            successore.send(oggetto)


@coroutine
def gestoreDiDefault(successore=None):
    while True:
        oggetto = (yield)
        print("Messaggio da gestoreDiDefault: non e`stato possibile gestire la richiesta {}". format(oggetto))
        if successore is not None:
            successore.send(oggetto)

class IDoNothing:
    def __init__(self, something):
        print("Hi")
        print(something)


class Client:
    def __init__(self):
        self.handler = gestore_int(writeInFile(), gestore_str(writeInFile(), gestoreDiDefault(gestore_tuple(None))))

    def entrust(self, objects):
        for o in objects:
            try:
                self.handler.send(o)
            except StopIteration:
                print("La catena ha smesso di accettare richieste")

        self.handler.close()


client = Client()
parole = ["ciao", 123456, "ma non", 987654, ("aa", "bbb", 123)]
client.entrust(parole)
