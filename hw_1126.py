# Watching Mooloo (Success)
import sys
input = sys.stdin.readline
input1 = list(map(int,input().split()))
watching_amount = input1[0]
basic_cost = input1[1]
watching_days = list(map(int,input().split()))
pay = basic_cost + 1
for i in range(watching_amount - 1):
    if watching_days[i + 1] - watching_days[i] - 1 > basic_cost:
        pay += basic_cost + 1
    else:
        pay += watching_days[i + 1] - watching_days[i]
print(pay)

# Rotate and Shift (Fail)
import sys
input = sys.stdin.readline
input1 = list(map(int,input().split()))
ord_len = input1[0]
act_posit_len = input1[1]
time = input1[2]
act_posit = list(map(int,input().split()))
for act_posit_idx in range(act_posit_len):
    act_posit[act_posit_idx] -= 1
    if act_posit[act_posit_idx] == -1:
        act_posit[act_posit_idx] = ord_len - 1
order = []
for ord_int in range(ord_len):
    order.append(ord_int)
for _ in range(time):
    for act_posit_int in range(act_posit_len):
        act_posit[act_posit_int] += 1
        if act_posit[act_posit_int] > ord_len - 1:
            act_posit[act_posit_int] = 0
    last_act_posit_order = order[act_posit[-1]]
    saved_int = order[act_posit[1]]
    for mov_idx in range(act_posit_len):
        if mov_idx == 0:
            order[act_posit[mov_idx + 1]] = order[act_posit[mov_idx]]
        elif mov_idx < act_posit_len - 1:
            order[act_posit[mov_idx + 1]] = saved_int
            saved_int = order[act_posit[mov_idx + 1]]
        else:
            order[act_posit[0]] = last_act_posit_order
for result in range(ord_len):
    if result < ord_len - 1:
        print(order[result],end=' ')
    else:
        print(order[result])

# Moo language
def solve():
    N, C, P = map(int, input().split()) # N은 단어 총 개수, C는 콤마 개수, D는 마침표 개수
    nouns, tverbs, iverbs, conjs = [], [], [], []   # 각 단어를 저장할 리스트 생성
    for _ in range(N):  # 모든 단어를 확인하면서 단어들을 알맞는 리스트에 append
        word, t = input().split()
        if t[0] == "n":
            nouns.append(word)
        if t[0] == "t":
            tverbs.append(word)
        if t[0] == "i":
            iverbs.append(word)
        if t[0] == "c":
            conjs.append(word)
    ans = (0, 0, 0, 0)  # 일단 ans 리스트는 0으로 채워져있음
    for n_tverb in range(len(tverbs) + 1):  # n_tverb는 사용 가능한 최대 tverbs의 개수를 나타냄
        n_iverb = min(len(iverbs), len(nouns) - 2 * n_tverb)    # n_iverb는 사용 가능한 최대 iverbs의 개수를 나타냄
        while n_iverb >= 0: # n_iverb가 0 이상일 동안
            n_conj = min(len(conjs), (n_tverb + n_iverb) // 2)  # n_conj은 사용 가능한 최대 conjs의 개수를 나타냄
            if n_tverb + n_iverb - n_conj <= P: # 마침표가 충분히 있을 때
                break
            n_iverb -= 1    # 마침표가 부족하면 n_iverb를 줄임
        if n_iverb < 0:
            continue
        extra_nouns = min(C, len(nouns) - (n_iverb + 2 * n_tverb))  # extra nouns는 사용 가능한 최대 콤마 뒤에 들어가는 nouns의 개수를 나타냄
        if n_tverb == 0:    # 만약 n_tverb가 0이라면
            extra_nouns = 0 # extra nouns는 사용 불가능
        n_words = 3 * n_tverb + 2 * n_iverb + n_conj + extra_nouns  # n_words는 최대 사용 가능한 단어의 개수를 나타냄
        ans = max(ans, (n_words, n_tverb, n_iverb, n_conj)) # n_words가 0이 아닌 이상 ans는 (n_words, n_tverb, n_iverb, n_conj)가 됨

    n_words, n_tverb, n_iverb, n_conj = ans # ans에 새로운 숫자들(n_words, n_tverb, n_iverb, n_conj)이 들어옴
    print(n_words)  # n_words print
    basic_sentences = [nouns.pop() + " " + iverbs.pop() for _ in range(n_iverb)] + [
        nouns.pop() + " " + tverbs.pop() + " " + nouns.pop() for _ in range(n_tverb)
    ]   # (noun + iverb) 형태의 문장들 생성, (noun + tverb + noun) 형태의 문장들 생성
    while n_tverb > 0 and C > 0 and len(nouns) > 0: # 만약 n_tverb가 0보다 크고(목적어는 t_verb가 있어야만 사용 가능) C가 0보다 크고(목적어 추가를 위한 콤마가 남아있음) noun 리스트의 길이가 0보다 클 때(목적어 추가를 위한 명사가 남아있음)
        basic_sentences[-1] += ", " + nouns.pop()   # basic sentences의 마지막에 콤마와 noun을 추가
        C -= 1  # 콤마 개수에서 1을 뺌
    compound_sentences = [
        basic_sentences.pop() + " " + conjs.pop() + " " + basic_sentences.pop()
        for _ in range(n_conj)
    ]   # basic sentences 2개를 conjs을 통해서 연결한 문장 생성
    sentences = [sentence + "." for sentence in basic_sentences + compound_sentences]   # 각 sentence 뒤에 마침표 붙임
    print(" ".join(sentences))  # sentences print


T = int(input())
for t in range(T):
    solve() # T번만큼 solve 함수를 실행

# Stamp grid
T = int(input())    # stamp grid 문제의 개수
for _ in range(T):
    input()
    N = int(input())    # stamp painting의 가로 세로 길이
    grid = [list(input()) for _ in range(N)]    # stamp painting을 격자로 나타냄
    K = int(input())    # stamp의 가로 세로 길이
    stamp = [input() for _ in range(K)] # stamp를 격자로 나타냄
    ans = [['.' for _ in range(N)] for _ in range(N)]   # 아무것도 칠해져있지 않은 grid를 나타냄
    for rot in range(4):    # rotate는 4번까지 가능함 (90도씩)
        for i in range(N-K+1):  # i는 현재 stamp의 가장 윗줄의 y좌표, range(N-K+1)은 stamp의 가장 윗줄이 grid에 찍힐 수 있는 모든 y좌표들
            for j in range(N-K+1):  # j는 현재 stamp의 가장 왼쪽 줄의 x좌표, range(N-K+1)은 stamp의 가장 왼쪽 줄이 grid에 찍힐 수 있는 모든 x좌표들
                if all(grid[i+a][j+b] == '*' or stamp[a][b] == '.' for a in range(K) for b in range(K)):    # stamp가 ans에 찍게 될 범위 안에 있는 격자가 전부 각각 stamp를 찍어야 하는 곳이거나 stamp가 찍어도 색칠이 안되는 부분일 때, a와 b는 둘 다 range(K)에 속해있는 모든 수
                    for a in range(K):  # a는 range(K)에 속해있는 모든 수
                        for b in range(K): # b도 range(K)에 속해있는 모든 수
                            if stamp[a][b] == '*':  # 만약 stamp의 [a][b] 위치의 격자가 '*'라면
                                ans[i+a][j+b] = '*' # ans의 [i+a][j+b] 위치의 격자도 '*'로 바꿈
        stamp = [[stamp[j][K-1-i] for j in range(K)] for i in range(K)] # stamp를 90도 회전시키기
    print("YES" if grid == ans else "NO")   # 만약 grid의 격자와 ans의 격자가 똑같다면 "YES" print, 아니면 "NO" print