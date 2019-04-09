
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


print(listsum([1,2,3,4,5]))


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]


print(repr(toStr(10, 2)))


from pythonds.basic.stack import Stack

rStack = Stack()


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ''
    while not rStack.isEmpty():
        res += str(rStack.pop())
    return res


print(toStr(10, 2))