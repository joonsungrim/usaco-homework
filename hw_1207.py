# Rotate and Shift
N, K, T = map(int, input().split()) # N = order의 길이, K는 active position의 개수, T는 시간
A = list(map(int, input().split())) + [N]   # A는 active position 리스트 + N
ans = [-1] * N  # ans는 -1이 N개 들어가있는 리스트
for i in range(K):  # i는 range(K) 안에 있음
    for j in range(A[i], A[i+1]):   # j는 active position의 i번째부터 i+1번째까지의 range 안에 있음 (만약 i가 active position의 마지막 숫자라면 A[i+1]은 존재하지 않기 때문에 order 리스트의 마지막 숫자인 N을 2번줄에서 A 리스트에 추가한 것임)
        T_prime = T - (j - A[i] + 1)
        if T_prime >= 0:
            increase_times = 1 + T_prime // (A[i+1] - A[i]) # j가 총 몇번 이동할지를 나타냄
            ending_position = (j + increase_times * (A[i+1] - A[i])) % N    # ending_position은 결과로 나올 리스트에서의 j의 인덱스를 나타냄
        else:
            ending_position = j # 결과로 나올 리스트에서의 j의 인덱스는 j
        ans[ending_position] = j    # ans 리스트의 ending_position 번째에 j를 넣음
print(" ".join(map(str, ans)))  # 결과 출력

# Astral Superposition
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    input1 = list(map(int,input().split()))
    grid_len = input1[0]
    move_right = input1[1]
    move_down = input1[2]
    star_str = ''
    for _ in range(grid_len):
        star_line = input()
        star_str += star_line
    star_list = list(star_str)
    B_list = []
    G_list = []
    counting_star = 0
    for i in star_list:
        if i == 'B':
            B_list.append(counting_star)
        if i == 'G':
            G_list.append(counting_star)
        counting_star += 1
    result = 0
    for i in B_list:
        if i % grid_len >= move_right and (i + 1) // grid_len >= move_down:
            prev_idx = i - ((grid_len * move_down) + move_right)
        if prev_idx >= 0:
            if star_list[prev_idx] not in ['G', 'B']:
                result = -1
                print(result)
                break
    noncounting_star = 0
    if result != -1:
        for i in G_list:
            if i % grid_len in range(move_right):
                pass
            elif (i + 1) // grid_len in range(move_down + 1):
                pass
            else:
                if (i + move_right) % grid_len < grid_len and (i + 1) // grid_len + move_down < grid_len:
                    next_idx = i + ((grid_len * move_down) + move_right)
                    if star_list[next_idx] != 'B':
                        noncounting_star += 1
                else:
                    noncounting_star += 1
        result = len(B_list) + len(G_list) - noncounting_star
        print(result)