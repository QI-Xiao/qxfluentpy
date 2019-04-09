
class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree!')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] +other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


v = Vector(5)
u = Vector(5)
v[1] = 23
v[-1] = 45
print('v[4]:',v[4])
alist = [1,2,3,4,5]
# u = v + alist
print(u)
total = 0
for entry in v:
    total += entry
print(total)
if u != v:
    print('aaaa')


class SequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

print('===============')
aaa = SequenceIterator([4,3,2,1])
print(next(aaa))
print(next(aaa))
print(next(aaa))
print(next(aaa))
sss = range(1,10,2)
print(type(sss))

class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length