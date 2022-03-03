import collections
import copy
import itertools
import time

Exam = collections.namedtuple("Exam", "name cfu")


class Observed:

    def __init__(self):
        self._obesrvers = set()

    def addObserver(self, observer, *observers):
        for o in itertools.chain((observer,), observers):
            self._obesrvers.add(o)
            o.update(self)

    def removeObserver(self, observer):
        self._obesrvers.discard(observer)

    def notify(self):
        for o in self._obesrvers:
            o.update(self)


class LaureaT_Student(Observed):

    def __init__(self, t_cfu=0, en_r=False, gr=collections.defaultdict()):
        super().__init__()
        self._total_cfu = t_cfu
        self._english_r = en_r
        self._grades = gr

    @property
    def total_cfu(self):
        return self._total_cfu

    @total_cfu.setter
    def total_cfu(self, value):
        if self._total_cfu != value:
            self._total_cfu = value
            super().notify()

    @property
    def english_r(self):
        return self._english_r

    @english_r.setter
    def english_r(self, value):
        if self._english_r != value:
            self._english_r = value
            super().notify()

    def add_grades(self, nome, voto):
        self._grades.update({nome: voto})

    @property
    def grades(self):
        return copy.deepcopy(self._grades)


class HistoryView:

    def __init__(self):
        self._lista = []

    def update(self, studente):
        self._lista.append((studente.total_cfu, studente.english_r, time.time()))


class LiveView:

    def __init__(self, studente):
        self._pre = studente.english_r
        self._precfu = studente.total_cfu

    def update(self, studente):
        if (self._pre != studente.english_r):
            self._pre = studente.english_r
            if (studente.english_r == True):
                print("Cambio stato: lo studente ha appena superato la prova di Inglese\n")

        if (self._precfu != studente.total_cfu):
            print("Cambio stato: lo studente ha superato un nuovo esame")
            print("Cambio stato: il numero di CFU e` : ", studente.total_cfu, "\n")
            self._precfu = studente.total_cfu


if __name__ == "__main__":
    tommaso = LaureaT_Student()
    list = LiveView(tommaso)
    hv = HistoryView()
    tommaso.addObserver(list, hv)

    tommaso.total_cfu = 1
    tommaso.total_cfu = 2
    tommaso.english_r = True
    tommaso.english_r = True
    tommaso.english_r = False
    tommaso.english_r = True
    tommaso.total_cfu = 2
    tommaso.total_cfu = 3
