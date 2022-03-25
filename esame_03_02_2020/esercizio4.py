import itertools
import time


class Observed:
    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)


class CorsoDiLaurea:
    studenti = {}
    mediaVotoLaurea = 0
    # True se voto > 100
    # False altrimenti
    mediaVotoLaureaOK = False
    numero_studenti = 0

    def __init__(self, nome, ultima_matricola):
        self.nome = nome
        self.ultima_matricola = ultima_matricola

    @property
    def mediaVotoLaurea(self):
        return self.mediaVotoLaurea

    @mediaVotoLaurea.setter
    def mediaVotoLaurea(self, value):
        self.mediaVotoLaurea = value

    @property
    def mediaVotoLaureaOK(self):
        return self.mediaVotoLaurea

    @mediaVotoLaureaOK.setter
    def mediaVotoLaureaOK(self, value):
        self.mediaVotoLaureaOK = value

    @property
    def numero_studenti(self):
        return self.numero_studenti

    @numero_studenti.setter
    def numero_studenti(self, value):
        self.numero_studenti = value


class Segreteria:
    numero_studenti = 0
    mediaVotoLaurea = 0
    mediaVotoLaureaOK = False

    def update(self, model):
        if model.numero_studenti > self.numero_studenti:
            print("Cambio stato: con le ultime immatricolazioni, il numero di studenti del Corso di Laurea in {} e` {}\n".format(model.nome, model.numero_studenti))
        elif model.numero_studenti < self.numero_studenti:
            print("Cambio stato: con le ultime immatricolazioni, il numero di studenti del Corso di Laurea in {} e` {}\n".format(model.nome, model.numero_studenti))

        if model.mediaVotoLaurea != self.mediaVotoLaurea:
            print("Cambio stato: con l'ultima seduta di Laurea, il voto medio del Corso di Laurea in {} e` uguale a {}\n".format(model.nome, model.mediaVotoLaurea))

        if (model.mediaVotoLaureaOK is False) and (model.mediaVotoLaureaOK == self.mediaVotoLaureaOK):
            print("Cambio stato: con l'ultima seduta di Laurea, il voto medio del Corso di Laurea in {} e` diventato superiore a 100\n".format(model.nome))
        elif (model.mediaVotoLaureaOK is True) and (model.mediaVotoLaureaOK == self.mediaVotoLaureaOK):
            print("Cambio stato: con l'ultima seduta di Laurea, il voto medio del Corso di Laurea in {} e` diventato minore o uguale di 100\n".format(model.nome))

class Storico:
    def __init__(self):
        self.data = []
        self.mediaVotoLaureaOK = False

    def update(self, model):
        if self.mediaVotoLaureaOK != model.mediaVotoLaureaOk:
            self.mediaVotoLaureaOK = model.mediaVotoLaureaOk
            tripla = (model.nome, model.mediaVotoLaurea, time.time())
            self.data.append(tripla)

    def storia(self):
        return self.data
