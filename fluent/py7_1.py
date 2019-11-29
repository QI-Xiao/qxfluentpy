def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


target()
print(target)


def f1(a):
    print(a)
    print(b)


def f2(a):
    print(a)
    print(b)
    b = 9


from dis import dis
print(dis(f1))
print(dis(f2))


def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    print(averager.__code__.co_varnames)
    print(averager.__code__.co_freevars)
    print(averager.__closure__)
    print(averager.__closure__[0].cell_contents)
    return averager


avg = make_average()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)