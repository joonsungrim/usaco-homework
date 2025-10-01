# Air Cownditioning
import sys
input = sys.stdin.readline
a = int(input())
b = input()
c = b.split()
d = list(map(int,c))
e = input()
f = e.split()
h = list(map(int,f))
for i in range(a):
    d[i] -= h[i]
j = []
k = []
for i in range(a):
    if d[i] > 0:
        j.append(d[i])
        k.append(0)
    elif d[i] < 0:
        k.append(-d[i])
        j.append(0)
    else:
        j.append(0)
        k.append(0)
l = 0
m = 0
n = 'A'
while sum(j) != 0:
    if n == 'A':
        if l == 0:
            if j[l] != 0:
                m += 1
        else:
            if j[l-1] == 0 and j[l] != 0:
                m += 1
    if n == 'B':
        if j[l] != 0:
            j[l] -= 1
    l += 1
    if l == a:
        l = 0
        if n == 'A':
            n = 'B'
        else:
            n = 'A'

o = 0
p = 0
q = 'A'
while sum(k) != 0:
    if q == 'A':
        if o == 0:
            if k[o] != 0:
                p += 1
        else:
            if k[o-1] == 0 and k[o] != 0:
                p += 1
    if q == 'B':
        if k[o] != 0:
            k[o] -= 1
    o += 1
    if o == a:
        o = 0
        if q == 'A':
            q = 'B'
        else:
            q = 'A'

r = m + p

print(r)

# Non-transitive dice(fail)

# Counting liars
import sys
input = sys.stdin.readline
a = int(input())
c = 0
G = []
L = []
for _ in range(a):
    b = input().split()
    if b[0] == 'G':
        G.append(int(b[1]))
    else:
        L.append(int(b[1]))
    if int(b[1]) > c:
        c = int(b[1])
g = max(G)
l = max(L)
d = max(g,l)
e = []
for _ in range(d):
    e.append(0)
print(G,L)