import datetime

# 입력: 월1 일1 월2 일2
m1, d1, m2, d2 = map(int, input().split())

# 기준 연도 설정 (같은 해 기준이면 아무 연도나 OK)

def num_of_days(m,d):
# 각 달의 일수 (윤년은 고려하지 않음)
    day_list = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
    total_days = 0
    for i in range(1,m):
        total_days+=day_list[i]
    total_days+=d

    return total_days
# 요일 리스트 (정상 순서)
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 출력
diff = 0 
diff = num_of_days(m2,d2) - num_of_days(m1,d1) 
while diff < 0 :
    diff += 7
print(weekdays[diff%7])
