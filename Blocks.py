import sys
input = sys.stdin.readline
a = int(input())

b = []
for _ in range(4):
    c = input()
    b.append(list(c))

for _ in range(a):
    aa = 0
    bb = 0
    d = []
    e = input()
    ee = list(e)
    for i in ee:
        f = []
        for j in range(4):
            if i in b[j]:
                f.append(j)
        d.append(f)
    for k in d:
        if len(k) == 0:
            aa += 1
    if aa >= 1:
        print('NO')
    else:
        if len(d) == 1:
            print('YES')
        elif len(d) == 2:
            for l in d[0]:
                for m in d[1]:
                    if l != m:
                        bb += 1
        elif len(d) == 3:
            for l in d[0]:
                for m in d[1]:
                    for n in d[2]:
                        if l != m and l != n and m != n:
                            bb += 1
        else:
            for l in d[0]:
                for m in d[1]:
                    for n in d[2]:
                        for o in d[3]:
                            if l != m and l != n and l != o and m != n and m != o and n != o:
                                bb += 1
        if bb >= 1:
            print('YES')
        if bb < 1 and aa == 0:
            print('NO')