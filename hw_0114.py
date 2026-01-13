n = int(input())
s = input()
lastG = -1
secondlastG = -1
lastH = -1
secondlastH = -1
# 현재로썬 lastG, secondlastG, lastH, secondlastH의 값들을 전부 -1로 설정함
ans = 0
for i in range(n):  # i는 range(0,n)에 속한 수
    if s[i] == 'G': # 만약 s의 i번째 알파벳이 G일 때
        secondlastG = lastG # secondlastG의 값이 lastG의 값으로 바뀜
        lastG = i   # lastG의 값이 i의 값으로 바뀜
    else:   # 만약 s의 i번째 알파벳이 H일 때
        secondlastH = lastH # secondlastH의 값이 lastH의 값으로 바뀜
        lastH = i   # lastH의 값이 i의 값으로 바뀜
    if i >= 2 and lastG != -1 and lastH != -1:  # 만약 G와 H가 각각 최소 한개씩은 있고 총 알파벳의 개수가 3 이상일 때
        if lastG <= i-3 or lastH <= i-3:    # s[i-2]부터 s[i] 사이까지의 3개의 알파벳이 모두 같을 때
            ans = ans + min(lastG, lastH) - min(secondlastG, secondlastH)   # ?
        else:   # s[i-2]부터 s[i] 사이까지의 3개의 알파벳이 모두 같지는 않을 때
            ans = ans + (i-2) - min(secondlastG, secondlastH)   # photo 안에 각각의 알파벳이 최소 2개 이상 있는 경우를 봄
    print(lastG,secondlastG,lastH,secondlastH,ans)
print(ans)