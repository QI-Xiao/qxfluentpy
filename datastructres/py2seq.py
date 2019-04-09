class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        return self


aaa = SequenceIterator([5,3,334])
print(aaa)
print(next(aaa))
print(iter(aaa))