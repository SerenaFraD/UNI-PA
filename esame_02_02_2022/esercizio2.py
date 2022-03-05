def decoraClasse(cls):
    cls.arg = []
    cls.kwarg = []

    oldinit = cls.__init__

    def newinit(self, *args, **kwargs):
        cls.arg = args
        cls.kwargs = kwargs
        oldinit(self, args, kwargs)

    def conQualiArgomenti():
        lista = [cls.arg]

        for k in cls.kwarg:
            lista.append(k)

        print(lista)

    setattr(cls, "__init__", newinit)
    setattr(cls, "conQualiArgomenti", conQualiArgomenti)
    return cls

@decoraClasse
class C:
    def __init__(self, *args, **kwargs):
        print("ahahah")


a = 10
c = C(a, "ciao", {"ciao": "miao"})
C.conQualiArgomenti()
