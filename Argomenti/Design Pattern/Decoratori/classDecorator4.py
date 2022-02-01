# Scrivere un decoratore di classe che, se applicato ad una classe, la modifica in modo che funzioni
# come se fosse stata derivata dalla seguente classe base. N.B. le classi derivate da ClasseBase non 
# hanno bisogno di modificare i metodi f() e g() e la variabile varC. Inoltre quando vengono create le 
# istanze di una classe derivata queste ’’nascono’’ con lo stesso valore di varI settato da __init__ di 
# ClasseBase.

def decorator(Classe):
    Classe.__init__ = ClasseBase.__init__

    Classe.varC = ClasseBase.varC
    Classe.f = ClasseBase.f
    Classe.g = ClasseBase.g

    return Classe


class ClasseBase:
    varC = 1000

    def __init__(self):
        self.varl = 10

    def f(self, v):
        print(v * self.varl)

    @staticmethod
    def g(x):
        print(ClasseBase.varC * x)


@decorator
class IDKSomethingAmazingIGuess:

    def whatAreYouWaitingFor(self):
        print("said Mr. Incredible")


c = IDKSomethingAmazingIGuess()
c.f(4)
IDKSomethingAmazingIGuess.g(3)
c.whatAreYouWaitingFor()
