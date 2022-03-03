# L1: lista di stringhe
# L2: lista di oggetti
def defFact(L1: list, L2: list):
    def decorator(function):
        def wrapper(self, *args, **kwargs):
            function(self)
            attributi = self.__dict__.keys()

            for i in range(0, len(L1)):
                if L1[i] not in attributi:
                    setattr(self, L1[i], L2[i])

        return wrapper
    return decorator


class Hello:
    @defFact(["a", "b", "c"], [1, 2, "di casa"])
    def __init__(self):
        self.a = 1111111
        self.b = "miao"


h = Hello()
print(h.__dict__.items())
