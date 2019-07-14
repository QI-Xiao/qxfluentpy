def unique3(S, start, stop):
    print(S, start, stop)
    if stop - start <= 1:
        print('step1')
        return True
    elif not unique3(S, start, stop-1):
        print('step2')
        return False
    elif not unique3(S, start+1, stop):
        print('step3')
        return False
    else:
        print('step4,S[start], S[stop-1]',S[start], S[stop-1])
        return S[start] != S[stop-1]

print(unique3([1,2,3], 0, 3))

def fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib(n-1)
        return (a+b, a)

print(fib(10))