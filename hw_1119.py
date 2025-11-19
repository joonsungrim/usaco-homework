# Reverse Engineering
import sys
input = sys.stdin.readline
inp_amount = int(input())
for i in range(inp_amount):
    int_inf = input().split()
    int_len = int(int_inf[0])
    line = int(int_inf[1])
    fir_num_list = []
    for j in range(int_len * 2):
        fir_num_list.append([])
    sec_int_list = []
    for line_num in range(line):
        line_list = input().split()
        sec_int_list.append(int(line_list[1]))
        fir_num_idx = 0
        for fir_num_int in line_list[0]:
            if fir_num_int == '0':
                fir_num_list[fir_num_idx * 2].append(line_num)
            else:
                fir_num_list[fir_num_idx * 2 + 1].append(line_num)
            fir_num_idx += 1

# Moo operation
import sys
input = sys.stdin.readline
inp_am = int(input())
for i in range(inp_am):
    moo_inp = list(input())
    len_moo = len(moo_inp)
    result = 0
    min_alph_ch = 2
    if not 'O' in moo_inp[1:-1]:
        result = -1
    else:
        for o in range(1,len_moo-1):
            alph_ch = 0
            if moo_inp[o] == 'O':
                if moo_inp[o-1] != 'M':
                    alph_ch += 1
                if moo_inp[o+1] != 'O':
                    alph_ch += 1
                if min_alph_ch > alph_ch:
                    min_alph_ch = alph_ch
    if result == -1:
        print(result)
    else:
        print(len_moo - 3 + min_alph_ch)

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
    ans = (0, 0, 0, 0)  # ?
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
        if n_tverb == 0:    # 만약 n_trverb가 0이라면
            extra_nouns = 0 # extra nouns는 사용 불가능
        n_words = 3 * n_tverb + 2 * n_iverb + n_conj + extra_nouns  # n_words는 최대 사용 가능한 단어의 개수를 나타냄
        ans = max(ans, (n_words, n_tverb, n_iverb, n_conj)) # ?

    n_words, n_tverb, n_iverb, n_conj = ans # ?
    print(n_words)  # n_words print
    basic_sentences = [nouns.pop() + " " + iverbs.pop() for _ in range(n_iverb)] + [
        nouns.pop() + " " + tverbs.pop() + " " + nouns.pop() for _ in range(n_tverb)
    ]   # (noun + iverb) + (noun + tverb + noun) 형태의 문장(basic_sentences)을 생성
    while n_tverb > 0 and C > 0 and len(nouns) > 0: # 만약 n_tverb가 0보다 크고 C가 0보다 크고 noun 리스트의 길이가 0보다 클 때
        basic_sentences[-1] += ", " + nouns.pop()   # basic sentences의 마지막에 콤마와 noun을 추가
        C -= 1  # C에서 1을 뺌
    compound_sentences = [
        basic_sentences.pop() + " " + conjs.pop() + " " + basic_sentences.pop()
        for _ in range(n_conj)
    ]   # basic sentences 2개를 conjs을 통해서 연결함
    sentences = [sentence + "." for sentence in basic_sentences + compound_sentences]   # sentence 뒤에 마침표를 붙임
    print(" ".join(sentences))  # sentence print


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
    for rot in range(4):    # 여기부터 이해 안됨
        for i in range(N-K+1):
            for j in range(N-K+1):
                if all(grid[i+a][j+b] == '*' or stamp[a][b] == '.' for a in range(K) for b in range(K)):
                    for a in range(K):
                        for b in range(K):
                            if stamp[a][b] == '*':
                                ans[i+a][j+b] = '*'
        stamp = [[stamp[j][K-1-i] for j in range(K)] for i in range(K)]
    print("YES" if grid == ans else "NO")