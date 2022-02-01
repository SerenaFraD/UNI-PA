# Scrivere nel file esercizio2.py un decoratore di classe decoratoreDiClasse che dota la classe
# decorata di un metodo di istanza elencaVariabili. Il metodo elencaVariabili è un generatore
# che restituisce un iteratore delle variabili di istanza di tipo int dell’istanza per cui è invocato.

def decoratoreDiClasse(cls):
    def elencaVariabili(self):
        lista = self.__dict__.items()

        for k, v in lista:
            if isinstance(v, int):
                yield k

    setattr(cls, "elencaVariabili", elencaVariabili)
    return cls


@decoratoreDiClasse
class C:
    def __init__(self):
        self.a = 1
        self.b = 2.1
        self.c = "casa"
        self.d = 4
        self.e = 5


prova = C()
for x in prova.elencaVariabili():
    print(x)
