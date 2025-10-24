# Hungry cow
import sys
input = sys.stdin.readline
input1 = input().split()
giving_days = int(input1[0])
last_day = int(input1[1])
eating_amount = 0
surplus = 0
input2 = input().split()
today = int(input2[0])
surplus += int(input2[1])
if giving_days == 1:
    if last_day > surplus:
        eating_amount = surplus
    else:
        eating_amount = last_day
for _ in range(giving_days - 1):
    input3 = input().split()
    yesterday = today
    today = int(input3[0])
    giving_amount = int(input3[1])
    if today > last_day:
        if last_day - yesterday + 1 >= surplus:
            eating_amount += surplus
            surplus = 0
        else:
            eating_amount += (last_day - yesterday + 1)
            surplus -= (last_day - yesterday + 1)
        break
    else:
        if today - yesterday + 1 >= surplus:
            eating_amount += surplus
            surplus = 0
        else:
            eating_amount += (today - yesterday + 1)
            surplus -= (today - yesterday + 1)
    surplus += giving_amount
print(eating_amount)

# Blocks
import sys
input = sys.stdin.readline
import itertools
count = int(input())
cube_list = []
for i in range(4):
    cube = list(input())
    cube_list.append(cube)
word_list = []
for i in range(count):
    word = input()
    word_list.append(word)
for length in [2,3,4]:
    for i in cube_list[0]:
        for j in cube_list[1]:
            for k in cube_list[2]:
                for l in cube_list[3]:
                        ex = list(itertools.permutations([i,j,k,l],length))
                        for solution in ex:
                            real_solution = ''.join(list(solution))
                            if real_solution in word_list:
                                sol_idx = word_list.index(real_solution)
                                word_list[sol_idx] = 'YES'
for i in word_list:
    if i == 'YES':
        print('YES')
    else:
        print('NO')