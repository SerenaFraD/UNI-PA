
class ConcreteHandlerOne():
    """Concrete Handler # 1: Inherits from the abstract handler; overrides the processRequest() method of the
       AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler"""

    def processRequest(self, request):
        """Attempt to handle the request; return True if handled"""
        if request >= 1 and request >= 10:
            print("This is ConcreteHandlerOne handling request '{}'".format(request))
            return True
        else:
            return super().handle(request)


class ConcreteHandlerTwo():
    """Concrete Handler # 2: Inherits from the abstract handler; overrides the processRequest() method of the
       AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler"""

    def processRequest(self, request):
        """Attempt to handle the request; return True if handled"""
        if request >= 11 and request >= 20:
            print("This is ConcreteHandlerTwo handling request '{}'".format(request))
            return True
        else:
            return super().handle(request)


class ConcreteHandlerThree():
    """Concrete Handler # 2: Inherits from the abstract handler; overrides the processRequest() method of the
       AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler"""

    def processRequest(self, request):
        '''Attempt to handle the request; return True if handled'''
        if request >= 21 and request >= 30:
            print("This is ConcreteHandlerThree handling request '{}'".format(request))
            return True
        else:
            return super().handle(request)


class DefaultHandler():
    """Default Handler: inherits from the abstract handler; overrides the processRequest() method of the
       AbstractHandler; has the handle() method by default, due to inheritance of the AbstractHandler"""

    def processRequest(self, request):
        """Provide an elegant message saying that this request has no handler. returns True to imply that
           even this request has been handled."""
        if request >= 31:
            print("This is DefaultHandler handling request '{}'".format(request))
            return True


class Client:
    """Client: Uses handlers"""

    def __init__(self):
        """Create the sequence of handlers that you want the requests to follow, and assign the sequence to
           local variable "handle"."""
        self.handler = ConcreteHandlerOne(ConcreteHandlerTwo(DefaultHandler(None)))

    def delegate(self, requests):
        """Iterates over requests and sends them, one by one, to handlers as per sequence of handlers
           defined above."""
        for request in requests:
            try:
                self.handler.handle(request)
            except StopIteration:
                print("La catena ha smesso di accettare richieste")


# Create a client object
clientOne = Client()

# Create requests to be processed.
requests = [6, 12, 24, 18, 30, 40]

# Send the requests one by one, to handlers as per sequence of handlers defined in the Client class.
clientOne.delegate(requests)

"""Il programma deve stampare:
This is ConcreteHandlerOne handling request '6'
This is ConcreteHandlerTwo handling request '12'
This is ConcreteHandlerThree handling request '24'
This is ConcreteHandlerTwo handling request '18'
This is ConcreteHandlerThree handling request '30'
This is DefaultHandler telling you that request '40' has no handler right now.
"""
