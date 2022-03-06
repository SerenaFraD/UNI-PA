def decFact(*pos_args, **keyw_args):
    # decoratore di classe
    def decoratore(cls):
        oldinit = cls.__init__

        def newInit(self, *args):
            oldinit(self, *args)

            attr = list(self.__dict__.keys())

            for i in range(len(pos_args)):
                if pos_args[i] not in attr:
                    setattr(self, str(pos_args[i]), None)

            for k, v in keyw_args.items():

                if k not in attr:
                    setattr(self, k, v)

        setattr(cls, "__init__", newInit)
        return cls

    return decoratore


d = {'uno': 'miao', 'due': 'ciao'}

@decFact('ciao', 'casa', 'x1', 'x2', **d)
class C:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3


c = C(1, 2, 3)
print(c.x1, c.x2, c.x3, c.ciao, c.casa, c.uno, c.due)
