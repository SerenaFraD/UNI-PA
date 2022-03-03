def decoratorFactory(t):
    def decoratoreDiClasse(cls):
        def elencaVariabili(self):
            lista = self.__dict__.items()

            for k, v in lista:
                if isinstance(v, t):
                    yield k

        setattr(cls, "elencaVariabili", elencaVariabili)
        return cls
    return decoratoreDiClasse


@decoratorFactory(str)
class C:
    def __init__(self):
        self.a = 1
        self.b = 2.1
        self.c = "casa"
        self.d = 4
        self.e = 5
        self.f = 2.1
        self.g = 2.1


prova = C()
for x in prova.elencaVariabili():
    print(x)
