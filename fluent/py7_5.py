from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    print('obj:', obj)
    content = html.escape(repr(obj))
    print('content:', content)
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize({1,2,3}))
print(htmlize(abs))
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(42))
print(htmlize(['alpha', 66, {3, 2, 1}]))
print(isinstance([1], abc.MutableSequence))
print(html.escape('x > 2 && x < 7'))
