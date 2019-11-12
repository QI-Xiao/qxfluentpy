from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        # yield 3
        # yield 4
        # yield 45
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        # for i in self:
        #     print(i)
        # print(*self)
        print('self: ', self, type(self))
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
    #     print(tuple(self))
        return str(tuple(self))
    #     return '123'

    def __bytes__(self):
        print()
        print(
            [ord(self.typecode)]

        )
        print(self)
        print(array(self.typecode, self))
        return (
            bytes([ord(self.typecode)]) +
            bytes(array(self.typecode, self))
        )

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


v1 = Vector2d(3, 4)
# print(v1.x, v1.y)
#
# x, y = v1
# print(x, y)
print(v1)
print(repr(v1))
print(bytes(v1))