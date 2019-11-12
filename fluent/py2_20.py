from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp2 = open('floats.bin', 'rb')
floats2.fromfile(fp2, 10**7)
fp2.close()
print(floats2[-1], floats == floats2)

a = array('d', (random() for j in range(10)))
print(a)
a = array(a.typecode, sorted(a))
print(a)
