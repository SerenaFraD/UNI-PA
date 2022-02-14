class Pacco:
    STATI = ("ordinato", "spedito", "ricevuto")
    ORDINATO = 0
    SPEDITO = 1
    RICEVUTO = 2

    d = {
        ORDINATO: (None, SPEDITO),
        SPEDITO: (ORDINATO, RICEVUTO),
        RICEVUTO: (ORDINATO, None)
    }

    def __init__(self):
        self.packageState = Pacco.ORDINATO

    @property
    def packageState(self):
        if self.succ != self._succ:
            return Pacco.RICEVUTO
        elif self.prev != self._prev:
            return Pacco.ORDINATO
        else:
            return Pacco.SPEDITO

    @packageState.setter
    def packageState(self, val):
        if val == Pacco.SPEDITO:
            self.prev = self._prev
            self.succ = self._succ
        elif val == Pacco.ORDINATO:
            self.prev = lambda *args: print("Non posso retrocedere di stato")
            self.succ = self._succ
        elif val == Pacco.RICEVUTO:
            self.prev = self._prev
            self.succ = lambda *args: print("Non posso avanzare di stato")

    def _prev(self):
        self.packageState = self.d[self.packageState][0]
        print(self.packageState)
        print(self.d[self.packageState][0])

    def _succ(self):
        self.packageState = self.d[self.packageState][1]

    def stampaStato(self):
        return Pacco.STATI[self.packageState]


def main():
    print("\nCreo il pacco")
    pacco = Pacco()
    pacco.stampaStato()
    print("\nInoltro il pacco all'ufficio postale")
    pacco.succ()
    pacco.stampaStato()
    print("\nConsegno il pacco al destinatario")
    pacco.succ()
    pacco.stampaStato()
    print("\nProvo a passare ad uno stato successivo")
    pacco.succ()
    pacco.stampaStato()


if __name__ == "__main__":
    main()

"""Il  programma deve stampare:
Creo il pacco
Il pacco e` stato ordinato ma non ancora spedito

Inoltro il pacco all'ufficio postale
Il pacco e` stato spedito ma non ancora ricevuto

Consegno il pacco al destinatario
Il pacco e` stato ricevuto 

Provo a passare ad uno stato successivo
Il pacco e` gia` stato ricevuto
Il pacco e` stato ricevuto 
"""
