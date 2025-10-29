# Cow college version 1
import sys
input = sys.stdin.readline
cow_amount = int(input())
max_pay = list(map(int,input().split()))
max_pay.sort()
max_pay_list = list(set(max_pay))
pay_sum_list = []
length = len(max_pay)
for i in max_pay_list:
    pay_sum = (length - max_pay.index(i)) * i
    pay_sum_list.append(pay_sum)
solution = max(pay_sum_list)
sol_idx = pay_sum_list.index(solution)
ind_pay = max_pay_list[sol_idx]
print(solution, ind_pay)
print(max_pay,max_pay_list)

# Cow college version 2
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