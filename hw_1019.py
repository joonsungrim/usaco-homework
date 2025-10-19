# Walking home
import sys
input = sys.stdin.readline
count = int(input())
for _ in range(count):
    nums = input()
    grid = int(nums[0])
    corner = int(nums[2])
    list = []
    for j in range(grid):
        line = input()
        for k in line:
            list.append(k)
    result = 0
    f = []
    if corner >= 1:
        if not 'H' in list[0:(grid)]:
            for m in range(1,grid+1):
                f.append(list[(m*grid)-1])
            if not 'H' in f:
                result += 1
        f = []
        if not 'H' in list[-(grid):]:
            for n in range(0,grid):
                f.append(list[n*grid])
            if not 'H' in f:
                result += 1
    f = []
    if corner >= 2:
        for o in range(2,grid):
            if not 'H' in list[grid*(o - 1):grid*(o)]:
                result += 1
            g = o
            for p in range(grid):
                f.append(list[(o-1)+(grid*p)])
            if not 'H' in f:
                result += 1
            f = []
    f = []
    g = []
    aa = []
    bb = 0
    cc = 0
    if corner >= 3:
        for q in range(grid-1):
            f.extend(list[grid*q + 1:grid*(q+1)])
            g.extend(list[(grid)*(q+1):grid*(q+2)-1])
        for r in f:
            if r == 'H':
                if cc == grid - 2:
                    pass
                elif cc in range(grid - 2) or (cc + 1) % (grid - 1) == 0:
                    bb += (grid - 2)
                else:
                    bb += ((grid - (cc // (grid - 1)))+(cc % (grid - 1)))
            cc += 1
        cc = 0
        for s in g:
            if s == 'H':
                if cc == (grid - 1) * (grid - 2):
                    pass
                elif cc % (grid - 1) == 0 or cc in range(((grid - 1) ** 2) - (grid - 2),grid ** 2):
                    bb += (grid - 2)
                else:
                    bb += ((cc // ((grid - 1)) - 1) + ((grid - 1) - (cc % (grid - 1))))
            cc += 1
        result += (((grid- 2 ) ** 2) * 2 - bb)

    print(result)

# Drought(Fail)

# Non-transitive dice
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
                                if h > k:
                                    if t < s and v > u:
                                        aa += 1
                                if h < k:
                                    if t > s and v < u:
                                        aa += 1
    if aa >= 1:
        print('yes')
    else:
        print('no')

# Blocks(Using permutation)(Fail)