def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1

aaa = count([1,1,1,3],1)
print(count([1,3,1],1))

def scale(data,factor):
    for j in range(len(data)):
        data[j] *= factor
print(scale([3,2,2],3))

aaa = max(1,-21,3,key=abs)
print(aaa)

bbb = [1,5,4,3]
print(bbb.sort())
print(bbb)

ccc = '1 2 3'

print(ccc)
print(type(ccc))
print(ccc.split())


def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise TypeError('x cannot be negative')

x = 'aa'
y = 5
try:
    print(x/y)
except (ZeroDivisionError,TypeError) as e:
    print(e)


def factor(n):
    k = 1
    while k*k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k ==n:
        yield k

print(sum(factor(100)))
for i in factor(100):
    print(i)


# def fibonacci():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         future = a + b
#         a = b
#         b =future
#
# for i in fibonacci():
#     if i <100:
#         print(i,'\n')
#     else:
#         break
n=-5
param = n if n >= 0 else -n
print(param)

n = 5
total = sum(k*k for k in range(1,n+1))
print(total)

ccc = {'a':11,'b':22}
for k,v in ccc.items():
    print(k)
    print(v)


def fibonacci(n):
    a, b = 0, 1
    while True:
        if a<n:
            print(a)
            a, b = b, a+b
        else:
            return


n = 50
fibonacci(n)