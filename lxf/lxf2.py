# -*- coding: utf-8 -*-


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'a', 'b', 'c')


def trim(s):
    while True:
        if s == '':
            break
        if s[0] == ' ':
            s = s[1:]
        elif s[-1] == ' ':
            s = s[:-1]
        else:
            break

    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


d = {'a': 1, 'b': 2, 'c': 3}

for key,vl in d.items():
    print(key,vl)

from collections import Iterable

print(isinstance('abc', Iterable))

def findMinAndMax(L):
    if L:
        min = L[0]
        max = L[0]
    else:
        return (None, None)
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i for i in L1 if isinstance(i, str)]

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a,b = b, a+b
        n = n+1
    return 'done'

print(fib(100))

def triangles():
    trilist = [1]
    while True:
        yield trilist
        trilist = [1] + [trilist[i]+trilist[i+1] for i in range(len(trilist)-1)] + [1]


aa = triangles()
for i in range(10):
    print(next(aa))

