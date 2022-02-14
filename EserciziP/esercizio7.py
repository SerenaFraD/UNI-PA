class ClsBase:
    a = 1
    b = 2

    @classmethod
    def addAttr(cls, s: str, v):
        if getattr(cls, s, True):
            setattr(cls, s, v)


class Cls(ClsBase):
    c = 3
    d = 4


ClsBase.addAttr("c", 3)
print(dir(ClsBase))
ClsBase.addAttr("a", 3)
print(dir(ClsBase))
Cls.addAttr("e", 3)
print(dir(Cls))
Cls.addAttr("d", 3)
print(dir(Cls))
Cls.addAttr("a", 3)
print(dir(Cls))
