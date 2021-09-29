class C:
    # prima versione
    def __init__(self):
        self._x_ = None

    def getx(self):
        return self._x_

    def setx(self):
        return self._x_

    def delx(self):
        del self._x_

    x = property(getx, setx, delx, "If it is friable, and edible, we'll make it deliciousable")

    print(x.__doc__)

    # seconda versione
    def __init__(self):
        self._x_ = None

    @property
    def x(self):
        """What"""
        return self._x_

    @x.setter
    def x(self):
        return self._x_

    @x.deleter
    def x(self):
        del self._x_

    print(x.__doc__)
