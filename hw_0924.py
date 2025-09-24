# Air cownditioning
import sys
input = sys.stdin.readline
a = int(input())
b = input()
c = b.split()
d = list(map(int,c))
e = input()
f = e.split()
h = list(map(int,f))
j = []
for i in range(len(d)):
    j.append(d[i] - h[i])
l = 0
while len(j) >= 1:
    k = []
    if j[0] == 0:
        j.pop(0)
        l += 1
    if len(j) != 0:
        if j[-1] == 0:
            j.pop(-1)
            l += 1
    if len(j) != 0:
        if j[0] < 0:
            for i in j:
                k.append(i+1)
            j = k
        if j[0] > 0:
            for i in j:
                k.append(i-1)
            j = k
print(l)

# Non-transitive dice (fail)

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
d = []
for _ in range(c):
    d.append(0)
for i in G:
    for j in range(i-1,c):
        d[j] += 1
for i in L:
    for j in range(i):
        d[j] += 1
e = max(d)
print(a-e)