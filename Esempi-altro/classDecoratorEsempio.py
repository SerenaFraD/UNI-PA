def count(aClass):
    aClass.numInstances = 0
    return aClass


@count
class Spam:
    @classmethod
    def count(cls):
        cls.numInstances += 1

    def __init__(self):
        self.count()


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

print("Instanzio un nuovo other")
other = Other()

print("Spam", spam.numInstances)
print("Sub", sub.numInstances)
print("Other", other.numInstances)
