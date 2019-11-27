import sys, re, collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)

print(index)

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy, d_proxy[1])
d[2] = 's'
print(d_proxy)
print(d_proxy[2])