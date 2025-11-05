# Leaders
N = int(input())    # 소의 마릿수
s = input() # 소의 종(G 또는 H)을 순서대로 배열
arr = list(map(int, input().split()))   # 각각의 소가 가지고 있는 리스트의 마지막 소의 순서
arr = [x - 1 for x in arr]  # 각각의 소가 가지고 있는 리스트의 마지막 소의 인덱스
eG, eH, lG, lH = -1, -1, -1, -1
for i in range(N - 1, -1, -1):  # i가 N-1부터 0까지 1씩 줄어듦 (s의 인덱스 역할)
    if (s[i] == 'G'):
        eG = i  # s 리스트에서 가장 앞에 있는 'G'의 인덱스를 구함
    if (s[i] == 'H'):
        eH = i  # s 리스트에서 가장 앞에 있는 'H'의 인덱스를 구함
for i in range(N):  # i가 0부터 N-1까지 1씩 늘어남 (s의 인덱스 역할)
    if (s[i] == 'G'):
        lG = i  # s 리스트에서 가장 뒤에 있는 'G'의 인덱스를 구함
    if (s[i] == 'H'):
        lH = i  # s 리스트에서 가장 뒤에 있는 'H'의 인덱스를 구함
print(arr)
print(eG,eH,lG,lH)
ans = 0
if (arr[eG] >= lG): # s 리스트에서 가장 앞에 있는 'G'가 가지고 있는 리스트의 마지막 소의 인덱스가 s 리스트에서 가장 뒤에 있는 'G'의 인덱스보다 크거나 같을 때 (자신과 같은 종인 소가 전부 자신의 리스트 안에 있다는 뜻)
    for i in range(eG): # i가 0에서 s 리스트에서 가장 앞에 있는 'G'의 인덱스보다 1 작은 숫자까지 1씩 늘어남
        if (i == eH):   # i가 s 리스트에서 가장 앞에 있는 'H'의 인덱스와 같을 때
            continue    # 계속 진행
        if (s[i] == 'H' and arr[i] >= eG):  # s 리스트의 i번째 알파벳이 'H'이고 i번째 소가 가지고 있는 리스트의 마지막 소의 인덱스가 s 리스트에서 가장 앞에 있는 'G'의 인덱스보다 크거나 같을 때
            ans += 1    # ans에 누적해서 1을 더함
if (arr[eH] >= lH): # s 리스트에서 가장 앞에 있는 'H'가 가지고 있는 리스트의 마지막 소의 인덱스가 s 리스트에서 가장 뒤에 있는 'H'의 인덱스보다 크거나 같을 때 (자신과 같은 종인 소가 전부 자신의 리스트 안에 있다는 뜻)
    for i in range(eH): # i가 0에서 s 리스트에서 가장 앞에 있는 'H'의 인덱스보다 1 작은 숫자까지 1씩 늘어남
        if (i == eG):   # i가 s 리스트에서 가장 앞에 있는 'G'의 인덱스와 같을 때
            continue    # 계속 진행
        if (s[i] == 'G' and arr[i] >= eH):  # s 리스트의 i번째 알파벳이 'G'이고 i번째 소가 가지고 있는 리스트의 마지막 소의 인덱스가 s 리스트에서 가장 앞에 있는 'H'의 인덱스보다 크거나 같을 때
            ans += 1    # ans에 누적해서 1을 더함
if ((arr[eG] >= lG or (eG <= eH and arr[eG] >= eH)) and (arr[eH] >= lH or (eH <= eG and arr[eH] >= eG))):   # (모르겠음)
    ans += 1
print(ans)

# FEB
import sys
input = sys.stdin.readline
amount = int(input())
cow_list = list(input())

# Feeding the cows
import sys
input = sys.stdin.readline
count = int(input())
for i in range(count):
    input1 = input()
    amount = int(input1[0])
    move = int(input1[1])
    cow_list = list(input())

# Air conditiong II
import sys
input = sys.stdin.readline
input1 = input().split()
for i in range(int(input1[0])):
    cow_inf = input()
for i in range(int(input[1])):
    air_inf = input()

# CowCollege
import sys
input = sys.stdin.readline
cow_amount = int(input())
max_pay = list(map(int,input().split()))
max_pay.sort()
max_pay_list = list(set(max_pay))
pay_sum_list = []
pay_amount_list = [[max_pay[0],cow_amount]]
for i in range(cow_amount):
    if i > 0:
        if max_pay[i] != max_pay[i - 1]:
            pay_amount_list.append([max_pay[i], cow_amount - i])
max_earn_list = []
for i in pay_amount_list:
    max_earn_list.append(i[0] * i[1])
maximum_money_amount = max(max_earn_list)
max_idx = max_earn_list.index(maximum_money_amount)
maximum_money_idx = pay_amount_list[max_idx][0]
print(maximum_money_amount,maximum_money_idx)