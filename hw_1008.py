import sys
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    aa = 0
    b = input()
    c = b.split()
    d = c[:4]
    e = list(map(int,d))
    f = c[4:]
    g = list(map(int,f))
    h = 0
    k = 0
    for i in range(4):
        for j in range(4):
            if e[i] < g[j]:
                h += 1
            if e[i] > g[j]:
                k += 1
    for l in range(1,11):
        for m in range(1,11):
            for n in range(1,11):
                for o in range(1,11):
                    p = [l,m,n,o]
                    s = 0
                    t = 0
                    u = 0
                    v = 0
                    for q in range(4):
                        for r in range(4):
                            if p[q] < e[r]:
                                s += 1
                            if p[q] > e[r]:
                                t += 1
                            if p[q] < g[r]:
                                u += 1
                            if p[q] > g[r]:
                                v += 1
                            if q == 3 and r == 3:
                                if h < k:
                                    if t < s and v > u:
                                        aa += 1
                                if h > k:
                                    if t > s and v < u:
                                        aa += 1
    if aa >= 1:
        print('yes')
    else:
        print('no')