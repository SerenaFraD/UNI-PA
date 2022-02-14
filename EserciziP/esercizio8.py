# Scrivere una classe che contiene un metodo che restituisce il numero
# di invocazioni degli altri metodi della classe.

class Conta:
    d = {"ciao": 0, "miao": 0}

    def __init__(self):
        pass

    def ciao(self):
        pass

    def miao(self):
        pass

    def __getattribute__(self, item):
        if super(Conta, self).__getattribute__(item):
            Conta.d[item] += 1
            return super(Conta, self).__getattribute__(item)


c = Conta()
c.ciao()
c.ciao()
c.ciao()
c.miao()
c.miao()
print(Conta.d)
