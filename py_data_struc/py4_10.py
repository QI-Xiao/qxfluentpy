class SSS:
    def __init__(self, name):
        self.__name__ = name

print(dir(SSS))

instance = SSS('abc')

print(SSS.__class__)
print(SSS.__class__.__name__)

print(instance.__class__)
print(instance.__class__.__name__)