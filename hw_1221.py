# Reflection
import sys
input = sys.stdin.readline
first_input = list(map(int,input().split()))
N = first_input[0]
U = first_input[1]
lines_list = [[],[],[],[]]
for _ in range(int(N/2)):
    line_input = list(input())
    lines_list[0].append(line_input[(int(N/2)):])
    lines_list[1].append(line_input[:(int(N/2))][::-1])
for _ in range(int(N/2)):
    line_input = list(input())
    lines_list[2].insert(0,line_input[:(int(N/2))][::-1])
    lines_list[3].insert(0,line_input[(int(N/2)):])
q1 = lines_list[0]
q2 = lines_list[1]
q3 = lines_list[2]
q4 = lines_list[3]
crd_list = []
chg_2_list = []
chg_num = 0
for i in range(int(N/2)):
    for j in range(int(N/2)):
        q_list = [q1[i][j], q2[i][j], q3[i][j], q4[i][j]]
        if q_list.count('.') == 0 or q_list.count('.') == 4:
            pass
        elif q_list.count('.') == 1:
            chg_num += 1
            dot_idx = q_list.index('.')
            if dot_idx == 0:
                crd_list.append([i+1,int(j+1+(N/2))])
            elif dot_idx == 1:
                crd_list.append([i+1,int((N/2)-j)])
            elif dot_idx == 2:
                crd_list.append([int(N-i),int((N/2)-j)])
            else:
                crd_list.append([N-i,int((N/2)+j+1)])
        elif q_list.count('.') == 3:
            chg_num += 1
            has_idx = q_list.index('#')
            if has_idx == 0:
                crd_list.append([i+1,int(j+1+(N/2))])
            elif has_idx == 1:
                crd_list.append([i+1,int((N/2)-j)])
            elif has_idx == 2:
                crd_list.append([int(N-i),int((N/2)-j)])
            else:
                crd_list.append([N-i,int((N/2)+j+1)])
        else:
            chg_num += 2
            dot_list = []
            has_list = []
            if q1[i][j] == '.':
                dot_list.append([i+1,int(j+1+(N/2))])
            if q1[i][j] == '#':
                has_list.append([i+1,int(j+1+(N/2))])
            if q2[i][j] == '.':
                dot_list.append([i+1,int((N/2)-j)])
            if q2[i][j] == '#':
                has_list.append([i+1,int((N/2)-j)])
            if q3[i][j] == '.':
                dot_list.append([int(N-i),int((N/2)-j)])
            if q3[i][j] == '#':
                has_list.append([int(N-i),int((N/2)-j)])
            if q4[i][j] == '.':
                dot_list.append([N-i,int((N/2)+j+1)])
            if q4[i][j] == '#':
                has_list.append([N-i,int((N/2)+j+1)])
            chg_2_list.extend([dot_list,has_list])
print(chg_num)
for _ in range(U):
    or_chg_num = chg_num
    sch_cor = list(map(int,input().split()))
    if sch_cor in crd_list:
        chg_num -= 1
        crd_list.remove(sch_cor)
    else:
        for i in chg_2_list:
            if sch_cor == i[0]:
                chg_num -= 1
                crd_list.append(i[1])
                break
            if sch_cor == i[1]:
                chg_num -= 1
                crd_list.append(i[0])
                break
    if or_chg_num == chg_num:
        chg_num += 1
    print(chg_num)