# Scrivere nel file moduloBase una classe di nome Base che contiene
# • una variabile di classe x inizializzata con il nome del modulo (l’assegnamento deve funzionare anche se rinominate il modulo)
# • un metodo print_x che stampa il nome della classe e il valore della variabile di classe x (nel caso Base venga estesa,
#   print_x deve stampare il nome della classe derivata e il valore della variabile x della classe derivata)
# • un metodo modifica_x che modifica a il valore della variabile di classe x con il valore passato come argomento(nel
#   caso Base venga estesa, modifica_x deve modificare il valore della variabile della classe derivata

class Base:
    x = __name__

    def print_x(self):
        print("Nome della classe ", __class__)
        print("Nome del modulo ", self.x)

    def modifica_x(self, attribute):
        self.x = attribute


b = Base()
b.print_x()
