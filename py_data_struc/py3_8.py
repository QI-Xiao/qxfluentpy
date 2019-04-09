from pythonds.basic.stack import Stack


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binstring = ''
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())

    return binstring


print(divideBy2(4))


def baseconverter(decNumber,base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binstring = ''
    while not remstack.isEmpty():
        binstring = binstring + digits[remstack.pop()]

    return binstring

print(divideBy2(4))

print(baseconverter(25,2))
print(baseconverter(25,16))