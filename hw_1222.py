# Block game
input_amount = int(input())
alph_list = [0 for _ in range(26)]
for _ in range(input_amount):
    words = (input().split())
    word_list_1 = [ord(i)-97 for i in words[0]]
    word_list_2 = [ord(i)-97 for i in words[1]]
    mt_list = []
    for i in word_list_2:
        if i not in word_list_1:
            mt_list.append(i)
        if i in word_list_1 and i not in mt_list:
            plus_amount = word_list_2.count(i) - word_list_1.count(i)
            if plus_amount > 0:
                mt_list.extend([i for _ in range(plus_amount)])
    word_list_1.extend(mt_list)
    for i in word_list_1:
        alph_list[i] += 1
for i in alph_list:
    print(i)
# 어떻게 blocks.in, blocks.out 형태로 바꾸는지 모르겠음