class C(object):
    __slots__ = ['varA', 'varB']

    def __setattr__(self, key, value):
        if key in self.__slots__:
            super().__setattr__(key, value)
        else:
            setattr(C, key, value)

    def __getattr__(self, item):
        if item in self.__slots__:
            return super().__getattribute__(item)
        else:
            return getattr(C, item)


"Qui comincia il codice per il test"
class D(C):
    def __init__(self, vz: int, vw: int):
        self.z = vz
        self.w = vw
        self.f = lambda x: vz * x


i1 = C()
i2 = C()
i1.varA = "a"
i2.varA = 4
i1.varB = "b"
i2.varB = 300
i1.x = 6

print("i valori di i1.varA, i1.varB e i1.x sono:", i1.varA, i1.varB, i1.x)
i2.x = 10
print("i valori di i1.varA, i1.varB e i1.x sono:", i1.varA, i1.varB, i1.x)
print("i valori di i2.varA, i2.varB e i2.x sono:", i2.varA, i2.varB, i2.x)
i1.y = 6
print("i valori di i1.varA, i1.varB e i1.y sono:", i1.varA, i1.varB, i1.y)
print("i valori di i2.varA, i2.varB e i2.y sono:", i2.varA, i2.varB, i2.y)
i3 = D(1000, 3000)
print("i valori di i3.z e i3.w sono:", i3.z, i3.w)
print("D.f(6)=", D.f(6))
i4 = D(4000, 8000)
print("i valori di i4.z e i4.w sono:", i4.z, i4.w)
print("i valori di i3.z e i3.w sono:", i3.z, i3.w)
print("D.f(6)=", D.f(6))

"""Il programma deve stampare:
i valori di i1.varA, i1.varB e i1.x sono: a b 6
i valori di i1.varA, i1.varB e i1.x sono: a b 10
i valori di i2.varA, i2.varB e i2.x sono: 4 300 10
i valori di i1.varA, i1.varB e i1.y sono: a b 6
i valori di i2.varA, i2.varB e i2.y sono: 4 300 6
i valori di i3.z e i3.w sono: 1000 3000
D.f(6)= 6000
i valori di i4.z e i4.w sono: 4000 8000
i valori di i3.z e i3.w sono: 4000 8000
D.f(6)= 24000
"""
