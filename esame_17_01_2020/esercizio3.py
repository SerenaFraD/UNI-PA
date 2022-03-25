import collections
from datetime import datetime


class Mediated:
    def __init__(self):
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.onchange(self)


class Mediator:
    def __init__(self, widgetCallablePairs):
        self.callablesForWidget = collections.defaultdict(list)
        for widget, caller in widgetCallablePairs:
            self.callablesForWidget[widget].append(caller)
            widget.mediator = self

    def onchange(self, widget):
        callables = self.callablesForWidget.get(widget)
        if callables is not None:
            for caller in callables:
                caller(widget)
        else:
            raise AttributeError("No on_change() method registered for {}".format(widget))


class Cane(Mediated):
    def __init__(self, nome: str, ora) -> None:
        super().__init__()
        self.nome = nome

        # ora in cui il cane ha mangiato l'ultima volta
        self.oraUltimoPasto = ora

    def abbaia(self):
        self.on_change()


class Persona(Mediated):
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome

        # se la persona è fuori casa questa variabile è settata a -1
        self.oraRitorno = 0

    def tornaACasa(self, ora):
        print("{} torna a casa alle ore {}".format(self.nome, ora.strftime('%H:%M')))
        self.on_change()

    def esce(self):
        print("{} esce di casa.".format(self.nome))
        self.oraRitorno = -1


class Casa:
    def __init__(self, nomePadrone: str, nomeCane1: str, nomeCane2: str, oraUltimaPappa1: datetime,
                 oraUltimaPappa2: datetime) -> None:

        self.allerta = False
        self.padrone = Persona(nomePadrone)

        self.cane1 = Cane(nomeCane1, oraUltimaPappa1)
        self.cane2 = Cane(nomeCane2, oraUltimaPappa2)

        self.create_mediator()

    def create_mediator(self):
        self.mediator = Mediator(((self.padrone, self.da_pappa), (self.cane1, self.allerta_padrone), (self.cane2, self.allerta_padrone)))

    def allerta_padrone(self, cane: Cane):
        print("Il cane {} abbaia".format(cane.nome))
        if self.padrone.oraRitorno == -1:
            self.allerta = True

    def da_pappa(self, padrone: Persona):
        if self.allerta:
            if (self.padrone.oraRitorno - self.cane1.oraUltimoPasto).total_seconds() / 60 / 60 > 4:
                print("{} da la pappa a {}".format(self.padrone.nome, self.cane1.nome))
                self.cane1.oraUltimoPasto = self.padrone.oraRitorno
            if (self.padrone.oraRitorno - self.cane2.oraUltimoPasto).total_seconds() / 60 / 60 > 4:
                print("{} da la pappa a {}".format(self.padrone.nome, self.cane2.nome))

            self.allerta = False


def main():
    casa = Casa("Maria", "pippo", "pluto", datetime(year=2020, month=1, day=11, hour=10),
                datetime(year=2020, month=1, day=11, hour=11))

    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.tornaACasa(datetime(year=2020, month=1, day=11, hour=15))
    casa.padrone.esce()


if __name__ == "__main__":
    main()
