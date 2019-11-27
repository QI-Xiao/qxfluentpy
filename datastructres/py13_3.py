def compute_kmp_fail(P):
    print('P', P)
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        print(P[k], P[j], k, j, m, fail)
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail


def find_kmp(T, P):
    n, m = len(T), len(P)
    print(n, m)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    print('fail:', fail)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1


# a = find_kmp('erefdwedfdffagjtyjfd', 'dffagjt')
# print(a)

# b = compute_kmp_fail('amalgamation')
# print('fail:', b)

b = compute_kmp_fail('abcabcaaaaabca')
print('fail:', b)