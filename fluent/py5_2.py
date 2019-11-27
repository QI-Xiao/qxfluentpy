class C:
    pass

def func(a=1,b=2):
    return 2, 3

print(sorted(set(dir(func)) - set(dir(C()))))
print(func.__annotations__)
print(func.__call__)
print(func.__closure__)
print(func.__code__)
print(func.__defaults__)
print(func.__get__)
print(func.__globals__)
print(func.__kwdefaults__)
print(func.__name__)
print(func.__qualname__)