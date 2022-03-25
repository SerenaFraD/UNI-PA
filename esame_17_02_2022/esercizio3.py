class ProteggiClasse:
    # proxy
    admitted = {"leggi", "scriviA", "scriviZ"}

    def __init__(self):
        self._implementazione = ClDaProteggere()

    def __getattr__(self, name):
        if name in self.admitted:
            return getattr(self._implementazione, name)
        else:
            raise AttributeError

class ClDaProteggere:
    def __init__(self):
        pass

    def leggi(self):
        print("Sono leggi")

    def scriviA(self):
        print("Sono scrivi A")

    def scriviZ(self):
        print("Sono scrivi Z")

    def ciao(self):
        print("Non dovrei essere chiamato")


p = ProteggiClasse()
p.leggi()
p.scriviA()
p.scriviZ()

try:
    p.ciao()
except AttributeError:
    print("Ok funziona")
