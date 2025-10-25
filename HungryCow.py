import sys
input = sys.stdin.readline
input1 = input().split()
giving_days = int(input1[0])    # haybale을 공급해주는 날의 수
last_day = int(input1[1])   # haybale을 공급하는 마지막 날
eating_amount = 0   # 지금까지 먹은 양
surplus = 0     # 남아있는 haybale의 양
input2 = input().split()
today = int(input2[0])      # 오늘이 몇번째 날인지
surplus += int(input2[1])
if giving_days == 1:    # haybale을 공급하는 날이 1일뿐일 때
    if last_day > surplus:  # haybale을 공급하는 마지막 날 > haybale의 양
        eating_amount = surplus
    else:       # haybale을 공급하는 마지막 날 <= haybale의 양
        eating_amount = last_day
for _ in range(giving_days - 1):    # 이미 input이 위에 하나 있었기 때문에 range(giving_days - 1)
    input3 = input().split()
    yesterday = today   # 오늘이었던 날을 예전으로 설정
    today = int(input3[0])
    giving_amount = int(input3[1])
    if today > last_day:    # 오늘 > 마지막 날
        if last_day - yesterday >= surplus: #예전과 오늘의 날 차이 >= 남아있는 haybale의 양
            eating_amount += surplus    # haybale을 전부 공급함
            surplus = 0 # haybale이 안 남음
        else:   # 예전과 오늘의 날 차이 < 남아있는 haybale의 양
            eating_amount += (last_day - yesterday) # haybale이 예전과 오늘의 날 차이 만큼 남아있음
            surplus -= (last_day - yesterday)   # haybale을 예전과 오늘의 날 차이 만큼 공급했으므로 그만큼 surplus에서 뺌
        break   # 이미 오늘이 마지막 날보다 이후이기 때문에 break
    else:   # 오늘 < 마지막 날
        if today - yesterday >= surplus:    # 예전과 오늘의 날 차이 >= 남아있는 haybale의 양
            eating_amount += surplus
            surplus = 0
        else:   # 예전과 오늘의 날 차이 < 남아있는 haybale의 양
            eating_amount += (today - yesterday)
            surplus -= (today - yesterday)
    surplus += giving_amount    # 공급받은 haybale을 surplus에 추가
print(eating_amount)