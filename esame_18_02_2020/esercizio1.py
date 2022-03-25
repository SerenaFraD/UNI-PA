import functools

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def handler_eq(successore=None):
    while True:
        stringa, carattere = (yield)
        if stringa is not None:
            if stringa[0:1] is carattere and stringa[0:1].isalpha():
                print("Richiesta {} gestista da handler_eq".format(stringa))
        if successore is not None:
            successore.send((stringa, carattere))

@coroutine
def handler_diff(successore=None):
    while True:
        stringa, carattere = (yield)
        if stringa is not None:
            if stringa[0:1].isalpha() and stringa[0:1] != carattere:
                print("Richiesta {} gestita da handler_diff: richiesta modificata".format(stringa))
                stringa = stringa[1:]
        if successore is not None:
            successore.send((stringa, carattere))

@coroutine
def handler_digit(successore=None):
    while True:
        stringa, carattere = (yield)
        if stringa is not None:
            if stringa[0:1].isdigit():
                print("Richiesta {} gestita da handler_digit".format(stringa))
        if successore is not None:
            successore.send((stringa, carattere))

@coroutine
def DefaultHandler(successore=None):
    while True:
        stringa, carattere = (yield)
        if stringa is None:
            print("Messaggio da DefaultHandler: non è stato possibile gestire la richiesta {}".format(stringa))


class Client:
    def __init__(self):
        self.handler = handler_diff(handler_eq(handler_digit(DefaultHandler(None))))

    def entrust(self, list1, list2):
        for i in range(0, len(list1)):
            try:
                self.handler.send((list1[i], list2[i]))
            except StopIteration:
                print("La catena ha smesso di accettare richieste")

        self.handler.close()


client = Client()
stringhe = ["ciao", "1234", "miao", "serena", None]
caratteri = ["c", "a", "-", "s", "a"]
client.entrust(stringhe, caratteri)
