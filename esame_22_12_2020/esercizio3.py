def decFact(t):
    def decoratore(cls):
        def riportaVariabiliDiClasse():
            attributes = [element for element in dir(cls) if not element.startswith("__")]
            classes = cls.__mro__
            for element in attributes:
                for classe in classes:
                    if element in classe.__dict__:
                        value = getattr(classe, element)
                        if isinstance(value, t):
                            yield (element, value, classe.__name__)

        setattr(cls, "riportaVariabiliDiClasse", riportaVariabiliDiClasse)
        return cls
    return decoratore

@decFact(int)
class A:
    aaa = 1
    bbb = 2
    ccc = 3

    def __init__(self):
        pass

@decFact(int)
class B(A):
    ddd = 4
    eee = 5
    fff = 6

    def __init__(self):
        pass


@decFact(int)
class C(B):
    ggg = 7
    hhh = 8
    iii = 9

    def __init__(self):
        pass


for var, value, classe in A.riportaVariabiliDiClasse():
    print("La variabile {} con valore {} e' nella classe {}".format(var, value, classe))
print("---------------------")

for var, value, classe in B.riportaVariabiliDiClasse():
    print("La variabile {} con valore {} e' nella classe {}".format(var, value, classe))
print("---------------------")

for var, value, classe in C.riportaVariabiliDiClasse():
    print("La variabile {} con valore {} e' nella classe {}".format(var, value, classe))
