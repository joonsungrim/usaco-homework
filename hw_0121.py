# Chip exchange
import sys
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    nums = list(map(int,input().split()))
    A = nums[0]
    B = nums[1]
    cA = nums[2]
    cB = nums[3]
    fA = nums[4]
    remain = fA - A
    final_a = remain
    if remain % cA != 0:
        final_b = int((final_a + (cA - (remain % cA))) / cA * cB)
    else:
        final_b = int(final_a / cA * cB)
    final_b -= B
    plan_c = int(remain - ((final_b - cB) / cB * cA) - 1)
    plan_c += final_b
    if final_b - B < 0 and plan_c - B < 0:
        print(0)
    else:
        print(max(final_b - B, plan_c - B))

# Cow splits
import sys
input = sys.stdin.readline
T, k = list(map(int,input().split()))
for _ in range(T):
    N = int(input())
    S = list(input())
    if N % 2 == 1:
        print(-1)
    else:
        num_list = [1 for _ in range(N * 3)]
        end_list = [[] for _ in range(int((N * 3) / 2))]
        for i in range(0, N * 3 - 1, 2):
            for j in range(i + 1, N * 3, 2):
                subq = S[i:j + 1]
                mid = int((j + 1 - i) / 2)
                if subq[:mid] == subq[mid:]:
                    end_list[int(i/2)].append(j + 1)
        num = 0
        if len(end_list[0]) != 0:
            loc = end_list[0][-1] 
            while loc < N * 3:
                if len(end_list[num]) == 0:
                    print(-1)
                    break
                loc = end_list[num][-1]
                num = int(loc / 2)
                for i in range(loc, N * 3):
                    num_list[i] += 1
        if loc == N * 3:
            print(num_list[-1])
            print(*num_list)

# Photoshoot
import sys
input = sys.stdin.readline
input1 = list(map(int,input().split()))
N = input1[0]
K = input1[1]
Q = int(input())
grid = []
for _ in range(N):
    line = [0 for _ in range(N)]
    grid.append(line)
for _ in range(Q):
    num_list = []
    sum_num = 0
    loc = list(map(int,input().split()))
    grid[loc[1] - 1][loc[0] - 1] = loc[2]
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            for k in range(i, i + K):
                for l in range(j, j + K):
                    sum_num += grid[k][l]
            num_list.append(sum_num)
            sum_num = 0
    print(max(num_list))