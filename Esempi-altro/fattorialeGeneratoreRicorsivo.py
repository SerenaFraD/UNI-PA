# continuazione esercizio1, ma con yield from
def myGenerator(n):
    return myGeneratorR(n, 1, 1)


def myGeneratorR(n, c, p):
    if n == 1:
        yield p
    else:
        yield p
        c += 1
        p = c * p
        yield from myGeneratorR(n - 1, c, p)


for f in myGenerator(5):
    print(f)
