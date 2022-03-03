def decFact(t):
    def decoratore(cls):
        @staticmethod
        def riportaVariabiliDiClasse():
            attributes = [element for element in dir(cls) if not element.startswith("__")]
            classes = cls.__mro__
            for element in attributes:
                for classe in classes:
                    if element in classe.__dict__:
                        value = getattr(classe, element)
                        if isinstance(value, t):
                            yield element, value, classe.__name__

        setattr(cls, "riportaVariabiliDiClasse", riportaVariabiliDiClasse)
        return cls
    return decoratore

@decFact(float)
class A:
    aaa = 1
    bbb = "buono"
    ccc = 3.1

    def __init__(self):
        pass

@decFact(str)
class B(A):
    ddd = 4.9
    eee = 5
    fff = "pare che"

    def __init__(self):
        pass


@decFact(float)
class C(B):
    ggg = 7
    hhh = 8.1
    iii = "funzioni"

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
