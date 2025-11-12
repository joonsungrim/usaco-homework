# Moo Language
import sys
input = sys.stdin.readline
inp_am = int(input())
for loop_1 in range(inp_am):
    sent_inf = list(map(int,input().split()))
    ele_am = [0,0,0,0,0]
    ele_am[4] = sent_inf[1]
    ele_am[3] = sent_inf[2]
    per_am = ele_am[3]
    for loop_2 in range(sent_inf[0]):
        word = input().split()
        if word[1] == 'noun':
            ele_am[0] += 1
        elif word[1] == 'transitive-verb':
            ele_am[1] += 1
        elif word[1] == 'intransitive-verb':
            ele_am[2] += 1
        else:
            ele_am[3] += 1
    if ele_am[3] > per_am * 2:
        ele_am[3] = per_am * 2
    used_word = 0
    trans_sent = 0
    while ele_am[3] > 0 and ele_am[0] > 0 and ele_am[1] + ele_am[2] > 0:
        if ele_am[3] < ele_am[0] and ele_am[0] >= 2 and ele_am[1] > 0:
            ele_am[3] -= 1
            ele_am[0] -= 2
            ele_am[1] -= 1
            used_word += 4
            trans_sent += 1
        elif ele_am[2] > 0:
            ele_am[3] -= 1
            ele_am[0] -= 1
            ele_am[2] -= 1
            used_word += 3
        else:
            if trans_sent > 0:
                if ele_am[0] > ele_am[4]:
                    used_word += ele_am[4]
                else:
                    used_word += ele_am[0]
            ele_am[0] = 0
    print(used_word)

# Stamp grid
inp_am = int(input())
for i in range(inp_am):
    line_am = int(input())
    lines = []
    for j in range(line_am):
        lines.extend(list(input()))
    stamp = []
    stamp_am = int(input())
    for j in range(stamp_am):
        stamp.extend(list(input()))

# Feeding the cows
def solve_one_case():
    n, k = map(int, input().split())    # n은 소가 몇마리인지 나타냄, k는 한 소의 위치에 먹이를 줄 때 인덱스가 얼마나 차이 나는 소한테까지 먹이를 줄 수 있는지 나타냄
    cows = input().strip()  # cows는 소들이 어떤 순서로 있는지 나타냄
    patches = ['.'] * n # patches 리스트는 n만큼의 '.'으로 차있음
    last_G = -k - 1 # 'G' 소들에게 먹이를 줄 수 있는 마지막 위치의 인덱스
    last_H = -k - 1 # 'F' 소들에게 먹이를 줄 수 있는 마지막 위치의 인덱스
    cnt = 0 # 먹이를 얼만큼 줘야 하는지 누적해서 더함

    for i, c in enumerate(cows):
        if c == 'G':    # 만약 현재 위치의 소가 'G'일 때
            if i - last_G > k:  # 만약 현재 위치에 있는 소가 아직 먹이를 받지 못했을 때
                place = min(i + k, n - 1)   # 현재 위치를 나타내는 place가 n 이상이 되지 못하게 함
                if patches[place] == 'H':   # 만약 patches 리스트의 place번째가 'H'일 때
                    place -= 1  # place에서 1을 뺌
                patches[place] = 'G'    # patches 리스트의 place번째를 'G'로 바꿈
                last_G = place  # place는 현재까지 나온 마지막 G의 인덱스를 나타냄
                cnt += 1    # cnt에 1을 더함

        elif c == 'H': # 만약 현재 위치의 소가 'H'일 때
            if i - last_H > k:  # 만약 현재 위치에 있는 소가 아직 먹이를 받지 못했을 때
                place = min(i + k, n - 1)   # 현재 위치를 나타내는 place가 n 이상이 되지 못하게 함
                if patches[place] == 'G':   # 만약 patches 리스트의 place번째가 'G'일 때
                    place -= 1  # place에서 1을 뺌
                patches[place] = 'H'    # patches 리스트의 place번째를 'H'로 바꿈
                last_H = place  # place는 현재까지 나온 마지막 H의 인덱스를 나타냄
                cnt += 1    # cnt에 1을 더함

    print(cnt) # cnt를 프린트함
    print("".join(patches))

t = int(input())    # t는 solve_one_case 함수가 몇번 돌아갈지 나타냄
for _ in range(t):  # t번만큼
    solve_one_case()    # solve_one_case 함수 실행

# Air Conditioning II
n, m = map(int, input().split())    # n은 소에 대한 설명이 몇 개인지, m은 에어컨에 대한 설명이 몇 개인지 나타냄
cows = [list(map(int, input().split())) for _ in range(n)]  # 소에 대한 설명이 n번 들어옴
acs = [list(map(int, input().split())) for _ in range(m)]   # 에어컨에 대한 설명이 m번 들어옴
min_cost = float('inf') # 최저값


def dfs(i, used):   # i에는 used 리스트로서 만들어질 수 있는 모든 리스트가 만들어질 때까지 1씩 더해짐, used 리스트에는 에어컨이 켜져있는 방들의 인덱스가 들어있음

    global min_cost # dfs 함수 밖에 있던 min_cost가 들어옴

    if i == m:  # 만약 현재 i의 값이 에어컨에 대한 설명이 들어온 횟수와 같다면
        cool = [0] * 101    # cool은 0이 101개 들어있는 리스트 (방의 개수가 100개이기 때문)
        cost = 0    # cost는 0
        for j in used:  # j는 used 리스트 안에 들어있는 수
            a, b, p, c = acs[j] # c는 특정 에어컨을 틀었을 때 써야하는 돈의 양
            cost += c   # cost에다가 c를 더함
            for x in range(a, b + 1):   # x가 인덱스인 방에 에어컨이 작동됨
                cool[x] += p    # x가 인덱스인 방에 온도 변화가 얼마나 일어났는지 cool 리스트에 기록

        for s, t, req in cows:  # s번째 방부터 s번째 방까지는 req도 이상의 온도 변화가 필요하다는 뜻
            for x in range(s, t + 1):   # x는 온도 조절이 필요한 방들의 인덱스
                if cool[x] < req:   # 온도 조절이 성공적으로 되었을 때
                    return  
        min_cost = min(min_cost, cost)  # 현재 cost가 min_cost보다 작으면 min_cost가 현재 cost의 값으로 바뀜
        return

    dfs(i + 1, used)    # i에다가 1을 더한 후 dfs 실행
    dfs(i + 1, used + [i])  # i에다가 1을 더한 값과 used 리스트에 i를 append한 후 dfs 실행

dfs(0, [])  # 맨 처음에는 i가 0이고 used 리스트는 비어있음

print(min_cost) # 지금까지 나왔던 cost들 중에서 가장 작은 숫자를 print