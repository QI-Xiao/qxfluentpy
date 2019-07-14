import time

a = range(1100)
b = range(1100)

start = time.time()
for i in ('%s %s' % (c, s) for c in a for s in b):
    # print(i)
    pass

end = time.time()

print('time', end - start)

start = time.time()
for i in ['%s %s' % (c, s) for c in a for s in b]:
    # print(i)
    pass

end = time.time()

print('time2', end - start)