def f(a, *, b):
    return a, b


print(f(1, b=2))
print(f.__defaults__)


def clip(text:str, max_len:'int > 0'=80) -> str:
    """在max_len前面或后面的第一个空格处截断文本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
            if end is None: # 没找到空格
                end = len(text)
    return text[:end].rstrip()


print('clip.__annotations__:', clip.__annotations__)
print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

from inspect import signature

sig = signature(clip)
print(sig, str(sig), sig.return_annotation)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
    note = repr(param.annotation).ljust(13)
    print(note)
    print()