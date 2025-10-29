# Cowcollege
import sys
input = sys.stdin.readline
cow_amount = int(input())
max_pay = list(map(int,input().split()))
max_pay.sort()
max_pay_list = [max_pay[0]]
for i in range(len(max_pay)):
    if i > 0:
        if max_pay[i] != max_pay[i - 1]:
            max_pay_list.append(1)
        else:
            max_pay_list[-1] += 1
max_pay = list(set(max_pay))
pay_sum_list = []
sum_cow = sum(max_pay_list)
for i in range(len(max_pay)):
    pay_sum_list.append(max_pay[i] * sum_cow)
    sum_cow -= max_pay_list[i]
max_money = max(pay_sum_list)
max_idx = pay_sum_list.index(max_money)
max_cow = max_pay[max_idx]
print(max_money,max_cow)

# Leaders
import sys
input = sys.stdin.readline
cow_amount = int(input())
cow_list = list(input())
leader_list = list(map(int,input().split()))
each_cow_list = []
each_cow_range = []
idx = 0
for i in leader_list:
    each_cow_list.append(cow_list[idx:i])
    each_cow_range.append([idx,i])
    idx += 1