class MyPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getValue(self):
        return self.value

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def setValue(self, newValue):
        self.value = newValue

    def __eq__(self, myPair):
        return self.key == myPair.getKey() and self.value == myPair.getValue()

    def __ne__(self, myPair):
        return self.key != myPair.getKey() or self.value != myPair.getValue()

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'
