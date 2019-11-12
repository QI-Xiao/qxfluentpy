class PriorityQueueBase:

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):

    def _find_min(self):
        if self.is_empty():
            raise IndexError('empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))


class Test:
    def __init__(self, p, e):
        self._p = p
        self._e = e

    def aaa(self):
        yield 1
        for i in range(3):
            yield i


a = Test(3,5)
b = Test(3,5)

print(Test(3,5))
print(Test(3,5))
print(a, b)
for i in a.aaa():
    print(i)

# a._p = 4
#
# print(a, b)
#
# print(a._p, b._p)