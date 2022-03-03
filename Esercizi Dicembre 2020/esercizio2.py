import functools

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def ConcreteHandlerOne(successor=None):
    while True:
        request = (yield)
        if 1 <= request <= 10:
            print("This is ConcreteHandlerOne handling request '{}'".format(request))
        elif successor is not None:
            try:
                successor.send(request)
            except StopIteration:
                break

@coroutine
def ConcreteHandlerTwo(successor=None):
    while True:
        request = (yield)
        if 11 <= request <= 20:
            print("This is ConcreteHandlerTwo handling request '{}'".format(request))
        elif successor is not None:
            try:
                successor.send(request)
            except StopIteration:
                break

@coroutine
def ConcreteHandlerThree(successor=None):
    while True:
        request = (yield)
        if 21 <= request <= 30:
            print("This is ConcreteHandlerThree handling request '{}'".format(request))
        elif successor is not None:
            try:
                successor.send(request)
            except StopIteration:
                break

@coroutine
def DefaultHandler(successor=None):
    while True:
        request = (yield)
        if request > 31:
            print("This is DefaultHandler telling you that request '{}' has no handler right now.".format(request))
        if successor is not None:
            successor.send(request)

class Client:
    """Client: Uses handlers"""

    def __init__(self):
        """Create the sequence of handlers that you want the requests to follow, and assign the sequence to
           local variable "handle"."""
        self.handler = ConcreteHandlerOne(ConcreteHandlerTwo(ConcreteHandlerThree(DefaultHandler(None))))

    def delegate(self, requests):
        """Iterates over requests and sends them, one by one, to handlers as per sequence of handlers
           defined above."""
        for request in requests:
            try:
                self.handler.send(request)
            except StopIteration:
                print("La catena ha smesso di accettare richieste")
        self.handler.close()


# Create a client object
client = Client()

# Create requests to be processed.
requests = [6, 12, 24, 18, 30, 40]

# Send the requests one by one, to handlers as per sequence of handlers defined in the Client class.
client.delegate(requests)

"""Il programma deve stampare:
This is ConcreteHandlerOne handling request '6'
This is ConcreteHandlerTwo handling request '12'
This is ConcreteHandlerThree handling request '24'
This is ConcreteHandlerTwo handling request '18'
This is ConcreteHandlerThree handling request '30'
This is DefaultHandler telling you that request '40' has no handler right now.
"""
