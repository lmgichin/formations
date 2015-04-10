def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[29-l] = n % 2
        n //= 2
        l += 1
    s= d.
    for p in xrange(1, 1 + l):
        ok = True
        for i in xrange(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1


print solution(955)