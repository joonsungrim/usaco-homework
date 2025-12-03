# Rotate and Shift
import sys
input = sys.stdin.readline
input1 = list(map(int,input().split()))
ord_len = input1[0]
act_posit_len = input1[1]
time = input1[2]
act_posit = list(map(int,input().split()))
order = []
for ord_int in range(ord_len):
    order.append(ord_int)
rev_act_posit_list = []
a = act_posit_len
while a > 0:
    a -= 1
    rev_act_posit_list.append(a)
for _ in range(time):
    last_order_int = order[act_posit[-1]]
    for i in rev_act_posit_list:
        if i == 0:
            order[act_posit[i]] = last_order_int
        else:
            order[act_posit[i]] = order[act_posit[i-1]]
    for i in range(act_posit_len):
        act_posit[i] += 1
        if act_posit[i] > ord_len - 1:
            act_posit[i] = 0
for i in order:
    if i != order[-1]:
        print(i,end = ' ')
    else:
        print(i)

# Roundabout rounding
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    result = 0
    N = input()
    len_N = len(N)
    if int(N) <= 48:
        fir_int = 1
        one_last_int = 44
    else:
        if int(N) < int('4' + '9' * (len_N - 1)):
            fir_int = int('4' + '9' * (len_N - 2))
            one_last_int = int('4' * len_N)
        else:
            fir_int = int('4' + '9' * (len_N - 1))
            one_last_int = int('4' * (len_N + 1))
    for ii in range(len(str(one_last_int)) - 2):
        i = ii + 1
        result += int('5' * i)
    if one_last_int < int(N):
        result += int(N) - one_last_int
    print(result)