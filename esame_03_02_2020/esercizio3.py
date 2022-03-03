# Si consideri la classe ClasseBase inserita tra i commenti nel file esercizio3.py. Si scriva un
# decoratore di nome ClasseBase che possa essere applicato ad una qualsiasi classe in modo
# che la classe cosi` decorata si comporti come se fosse derivata da ClasseBase

def classeBase(cls):
    def newInit(self):
        ClasseBase.__init__(self)

    setattr(cls, "__init__", newInit)

    methods = [(k, v) for k, v in ClasseBase.__dict__.items() if not k.startswith("__")]
    for k, v in methods:
        setattr(cls, k, v)

    return cls


class ClasseBase:
    def __init__(self):
        print("sono classe base")

    def ciao(self):
        print("Something ClasseBase")

    def miao(self):
        print("Something Miaomiao")


@classeBase
class ClasseDec:
    def __init__(self):
        print("Sono classe dec")

    def ciao(self):
        print("Something ClasseDec")


c = ClasseDec()
c.ciao()
c.miao()
