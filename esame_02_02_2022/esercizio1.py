import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def gestore_0_100(successore=None):
    while True:
        richiesta = (yield)
        if 0 <= richiesta <= 100:
            print("Richiesta {} gestita da gestore_0_100".format(richiesta))
        if successore is not None:
            try:
                successore.send(richiesta)
            except StopIteration:
                print("La catena ha smesso di funzionare")

@coroutine
def gestore_101_200(successore=None):
    while True:
        richiesta = (yield)
        if 101 <= richiesta <= 200:
            print("Richiesta {} gestita da gestore_101_200".format(richiesta))
        if successore is not None:
            try:
                successore.send(richiesta)
            except StopIteration:
                print("La catena ha smesso di funzionare")

@coroutine
def gestore_negativo(successore=None):
    while True:
        richiesta = (yield)
        if richiesta < 0:
            print("Richiesta {} gestita da gestore_negativo: la catena smette di funzionare".format(richiesta))
            break

        if successore is not None:
            try:
                successore.send(richiesta)
            except StopIteration:
                print("La catena ha smesso di funzionare")

@coroutine
def gestoreDiDefault(successore=None):
    while True:
        richiesta = (yield)
        if richiesta > 200:
            print("Messaggio da gestoreDiDefault: non e` stato possibile gestire la richiesta {}".format(richiesta))

        if successore is not None:
            try:
                successore.send(richiesta)
            except StopIteration:
                print("La catena ha smesso di funzionare")


class Client:
    def __init__(self):
        self.handler = gestore_0_100(gestore_101_200(gestore_negativo(gestoreDiDefault(None))))

    def delegate(self, requests):
        for r in requests:
            try:
                self.handler.send(r)
            except StopIteration:
                print("La catena ha smesso di funzionare")


client = Client()
richieste = [101, 99, 300, -100]
client.delegate(richieste)
