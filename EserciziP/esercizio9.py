# Scrivere un decorator factory che genera un decoratore di classe che
# dota la classe di un metodo che restituisce il numero di invocazioni
# del metodo passato come parametro al decorator factory.

# decorator factory
def decorator(method):
    # decoratore di classe
    def decClasse(classe):
        classe.numInvocazioni = 0
        oldMethod = getattr(classe, method)

        def newMethod(*args, **kwargs):
            classe.numInvocazioni += 1
            return oldMethod(*args, **kwargs)

        setattr(classe, method, newMethod)

        @staticmethod
        def numTimes():
            return classe.numInvocazioni

        setattr(classe, "numTimes", numTimes)

        return classe
    return decClasse


@decorator("__init__")
class C:
    def __init__(self):
        print("init")

    def ciao(self):
        print("ciao")

    def miao(self):
        print("miao")


c = C()
print("Prima di chiamare", c.numTimes())
c.ciao()
c.ciao()
print("Ciao 2 volte", c.numTimes())
c.miao()
print("Miao 1 volta", c.numTimes())
