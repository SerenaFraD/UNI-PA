# aClass nella invocazioni è Spam, Other o Sub
def count(aClass):
    aClass.numInstances = 0
    oldInit = aClass.__init__

    # self nelle invocazioni è Spam
    def __newInit__(self, *args, **kwargs):
        # questo if evita che instances di spam venga incrementato anche quando sono instanziati i suoi sub
        if aClass == type(self):
            aClass.numInstances += 1
        oldInit(self, *args, **kwargs)

    aClass.__init__ = __newInit__
    return aClass


@count
class Spam:
    pass


@count
class Sub(Spam):
    pass


@count
class Other(Spam):
    pass


# Prova
spam = Spam()
sub = Sub()
other = Other()

print("Spam", spam.numInstances)
print("Sub", sub.numInstances)
print("Other", other.numInstances)

print("Instance new other")
other = Other()

print("Spam", spam.numInstances)
print("Sub", sub.numInstances)
print("Other", other.numInstances)
