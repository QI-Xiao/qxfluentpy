with open('test.txt', 'r') as f:
    # for line in f.readlines():
    #     print(repr(line))
    #     print(line.strip())
    print(repr(f.read()))

from io import StringIO, BytesIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())