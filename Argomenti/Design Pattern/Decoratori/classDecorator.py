def count(aClass):
    aClass.numInstances = 0
    return aClass


@count
class Spam:
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1


class Sub(Spam):
    pass


class Other(Spam):
    pass


#Prova
spam = Spam()
sub = Sub()
other = Other()

print(spam.numInstances)
print(sub.numInstances)
print(other.numInstances)
