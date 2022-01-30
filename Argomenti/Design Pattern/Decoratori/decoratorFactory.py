# Scrivere un decorator factory che prende in input un tipo t
# genera un decoratore di classe che dota la classe di un metodo
# per contare il numero di variabili di istanza di tipo t
# dell’istanza per cui è invocato

# factory che accetta parametri
def factory(type):
    # vero decoratore
    def decoratore(Classe):
        def countVarOfType(self):
            number = 0

            for key, value in Classe.__dict__.items():
                if isinstance(value, type) and key != '__module__':
                    number += 1
            return number

        Classe.countVarOfType = countVarOfType
        return Classe

    return decoratore

@factory(int)
class Hey:
    ciao = 3.4
    casa = 8
    miao = float(3.4)
    pc = float(3.4)
    variabile = "ciao"
    va = "ciao"

    def funzione(self):
        pass


c = Hey()
print(c.countVarOfType())
