import itertools
from typing import Dict


def main():
    # stessa vista per i due libri osservati
    IV = VistaIst()

    # se il vostro codice non funziona con un'unica vista di tipo VisitIst allora togliete il commento alla linea qui sotto
    # e sostituite IVbis al posto di IV nella linea 25

    # IVbis=VistaIst()

    bibliotecaCentrale = Biblioteca("Biblioteca Centrale")
    libreriaMandetori = Libreria("Libreria Mandetori")
    libreriaFaltranella = Libreria("Libreria Faltranella")
    libroCPiuPiu = Libro("C++", [])
    libroJava = Libro("Java per tutti", [libroCPiuPiu])
    libroJava.observers_add(IV)
    libroPython = Libro("Python versus Java", [libroJava, libroCPiuPiu])
    libroOOP = Libro("OOP fundamentals", [libroJava, libroPython, libroCPiuPiu])
    libroOOP.observers_add(IV)

    print("La biblioteca centrale acquisisce \"Java per tutti\"\n")
    bibliotecaCentrale.compra(libroJava)
    print("I riferimenti di \"{}\" sono {}\n".format(libroJava.titolo,
                                                     [(x, y.titolo) for x, y in libroJava.riferimenti.items()]))
    print("La libreria Faltrenella compra 199 copie di \"{}\"\n".format(libroJava.titolo))
    libreriaFaltranella.compra(libroJava, 199)
    print("La biblioteca centrale acquisisce \"{}\"\n".format(libroOOP.titolo))
    bibliotecaCentrale.compra(libroOOP)
    print("I riferimenti di \"{}\" sono {}\n".format(libroOOP.titolo,
                                                     [(x, y.titolo) for x, y in libroOOP.riferimenti.items()]))
    print("La libreria Faltrenella compra 100 copie di \"{}\"\n".format(libroOOP.titolo))
    libreriaFaltranella.compra(libroOOP, 100)
    print("La {} compra 48 copie di  \"{}\"\n".format(libreriaMandetori.nome, libroOOP.titolo))
    libreriaMandetori.compra(libroOOP, 48)
    print("Proviamo a modificare i riferimenti di libroCPiuPiu")
    try:
        libroCPiuPiu.riferimenti[1] = libroPython
    except RuntimeError:
        print("Errore: non e` possibile modificare i riferimenti del libro\n")

    print("I riferimenti di \"{}\" sono {}\n".format(libroCPiuPiu.titolo,
                                                     [(x, y.titolo) for x, y in libroCPiuPiu.riferimenti.items()]))


class fruitore:
    def __init__(self, nome):
        self.nome = nome

    def compra(self, libro, num=1):
        libro.numero_copie += num


class Biblioteca(fruitore):

    def compra(self, libro):
        super().compra(libro)


class Libreria(fruitore):
    pass


class Observed:

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for o in itertools.chain((observer,), observers):
            self.__observers.add(o)
            o.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    # aggiungere il metodo notify
    def observers_notify(self, ob):
        for observer in self.__observers:
            observer.update(ob)


class Mydict(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.full = False

    def __setitem__(self, key, value):
        if self.full:
            raise RuntimeError()


class Libro(Observed, dict):
    titolo = ""
    _numero_copie = 0
    _alta_progressione = False
    riferimenti = None

    def __init__(self, titolo: str, lista: list):
        super().__init__()
        self.titolo = titolo
        self.riferimenti = Mydict()
        i = 0
        for element in lista:
            self.riferimenti[i] = element
            i += 1
        self.riferimenti.full = True

    @property
    def numero_copie(self):
        return self._numero_copie

    @numero_copie.setter
    def numero_copie(self, value: int):
        if self._numero_copie == 0:
            self._numero_copie += value
        else:
            if value >= (self._numero_copie * 2):
                self._alta_progressione = True

            elif value <= (self._numero_copie * 2):
                self._alta_progressione = False

            self._numero_copie += value
            super().observers_notify(self)

    @property
    def alta_progressione(self):
        return self._alta_progressione

    @alta_progressione.setter
    def alta_progressione(self, value: int):
        self._alta_progressione = value


class VistaIst:
    def __init__(self):
        self.raddoppio = False
        self.vendite = 0

    def update(self, obs):
        if self.raddoppio != obs.numero_copie:
            if self.raddoppio == obs.alta_progressione:
                if self.raddoppio:
                    print(
                        "Cambio stato: con l'ultimo acquisto, il libro '{}' ha piu` che raddoppiato le vendite\n".format(
                            obs.titolo, obs.numero_copie))
                else:
                    print(
                        "Cambio stato: con l'ultimo acquisto, le vendite di '{}' sono aumentate meno della meta\n".format(
                            obs.titolo, obs.numero_copie))
            print("Cambio stato: nuove vendite del libro '{}' per un totale di copie vendite pari a {} \n".format(
                obs.titolo, obs.numero_copie))

        self.raddoppio = obs.alta_progressione
        self.vendite = obs.numero_copie


class VistaStorica:
    pass


if __name__ == "__main__":
    main()

"""Il programma deve effettuare le seguenti stampe :

La biblioteca centrale acquisisce "Java per tutti"

Cambio stato: nuove vendite del libro "Java per tutti" per un totale di copie vendite pari a 1 

Cambio stato: con l'ultimo acquisto, il libro "Java per tutti" ha piu` che raddoppiato le vendite

I riferimenti di "Java per tutti" sono [(0, 'C++')]

La libreria Faltrenella compra 199 copie di "Java per tutti"

Cambio stato: nuove vendite del libro "Java per tutti" per un totale di copie vendite pari a 200 

Cambio stato: con l'ultimo acquisto, il libro "Java per tutti" ha piu` che raddoppiato le vendite

La biblioteca centrale acquisisce "OOP fundamentals"

Cambio stato: nuove vendite del libro "OOP fundamentals" per un totale di copie vendite pari a 1 

Cambio stato: con l'ultimo acquisto, il libro "OOP fundamentals" ha piu` che raddoppiato le vendite

I riferimenti di "OOP fundamentals" sono [(0, 'Java per tutti'), (1, 'Python versus Java'), (2, 'C++')]

La libreria Faltrenella compra 100 copie di "OOP fundamentals"

Cambio stato: nuove vendite del libro "OOP fundamentals" per un totale di copie vendite pari a 101 

Cambio stato: con l'ultimo acquisto, il libro "OOP fundamentals" ha piu` che raddoppiato le vendite

La Libreria Mandetori compra 48 copie di  "OOP fundamentals"

Cambio stato: nuove vendite del libro "OOP fundamentals" per un totale di copie vendite pari a 149 

Cambio stato: con l'ultimo acquisto, le vendite di "OOP fundamentals" sono aumentate meno della meta`

Proviamo a modificare i riferimenti di libroCPiuPiu
Errore: non e` possibile modificare i riferimenti del libro

I riferimenti di "C++" sono []
"""
