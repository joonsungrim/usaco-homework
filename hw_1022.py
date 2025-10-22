# Alchemy
import sys
input = sys.stdin.readline
amount = int(input())
list_input = input().split()
list = []
for i in list_input:
    list.append(int(i))
mix_list = []
for i in range(amount):
    mix_list.append([])
count = int(input())
for i in range(count):
    line = input().split()
    mix_list[int(line[0]) - 1] = line
for i in mix_list:
    mix = []
    if len(i) != 0:
        for j in i:
            mix.append(int(j))
        min_list = []
        for k in mix[2:]:
            min_list.append(list[k - 1])
        min_mix = min(min_list)
        for l in mix[2:]:
            list[l - 1] -= min_mix
        list[mix[0] - 1] += min_mix
print(list[-1])