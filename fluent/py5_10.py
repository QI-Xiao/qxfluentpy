from functools import reduce
from operator import mul

def multiply(a, b):
    return a * b


def fact(n):
    # return reduce(multiply, range(1, n+1))
    # return reduce(lambda a, b: a*b, range(1, n+1))
    return reduce(mul, range(1, n+1))

print(fact(4))

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
print()

for city in sorted(metro_data, key=lambda i: i[1]):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

cc_name = itemgetter(1,2,3)
for city in metro_data:
    print(cc_name(city))

from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [
    Metropolis(name, cc, pop, LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_data
]
# print(metro_areas)
print(metro_areas[0])
print(metro_areas[0].coord.lat)

from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(attrgetter('name', 'coord.lat')(city))

import operator
dir_operator = [name for name in dir(operator) if not name.startswith('__')]
print(dir_operator)

from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
print(methodcaller('replace', ' ', '-')(s))

from operator import mul
from functools import partial
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))


import unicodedata, functools

nfc = functools.partial(unicodedata.normalize, 'NFC')
print(nfc('café') == nfc('cafe\u0301'), nfc.func, nfc.args, nfc.keywords)