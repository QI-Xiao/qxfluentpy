registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'
              % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')
# print(registry)

@register()
def f2():
    print('running f2()')
# print(registry)

def f3():
    print('running f3()')


if __name__ == '__main__':
    print(registry)
    print(register()(f3))
    print(registry)
    print(register(active=False)(f2))
    print(registry)