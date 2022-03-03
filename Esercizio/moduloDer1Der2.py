# Scrivere nel file moduloDer1Der2 le seguenti classi che estendono Base di moduloBase:
# • Der1 che contiene una variabile di classe di nome x e niente altro
# • Der2 che contiene 0 variabili di classe e esattamente 6 metodi:
# • 3 di questi 6 metodi (uno statico, uno di classe e uno di instanza) stampano il valore della variabile x della classe base
# • gli altri 3 metodi (uno statiuno di classe e uno di instanza) stampano il valore della variabile x della classe stessa
# (NB: anche se all’inizio x di Der2 è di fatto x di Base poi le cose possono cambiare)

from Esercizio.moduloBase import Base

class Der1(Base):
    x = None


class Der2(Base):
    @staticmethod
    def printStatic():
        print(Base.x)

    @classmethod
    def printClass(cls):
        print(Base.x)

    def printNormale(self):
        print(Base.x)

    @staticmethod
    def printStatic2():
        print(Der2.x)

    @classmethod
    def printClass2(cls):
        print(cls.x)

    def printNormale2(self):
        print(self.x)
