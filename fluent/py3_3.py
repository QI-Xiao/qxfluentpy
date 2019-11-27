import builtins
from collections import ChainMap

def collection_test2():
    a = {"name": "leng"}
    b = {"age": 24}
    c = {"wife": "qian"}
    pylookup = ChainMap(a,b,c)
    print(pylookup)
    print(pylookup['age'],pylookup.maps)
    pylookup.update({"age": 25})
    print(pylookup)
    b['age'] = 26
    print(pylookup)
    print(type(pylookup.maps), type(pylookup))
    pylookup.maps[0]['age']=20
    pylookup.maps[1]['age']=22
    print(pylookup)
    print("-----------")
    d = {"name": "leng"}
    e = {"name":"123"}
    cm = ChainMap(d,e)
    print(cm)
    print(cm['name'])
collection_test2()


pylookup2 = ChainMap(locals(), globals(), vars(builtins))
print(pylookup2)

import collections

ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaazzz')
print(ct)
print(ct.most_common(3))