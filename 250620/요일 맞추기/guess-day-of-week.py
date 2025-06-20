import datetime

# 입력: 월1 일1 월2 일2
m1, d1, m2, d2 = map(int, input().split())

# 기준 연도 설정 (같은 해 기준이면 아무 연도나 OK)

# 각 달의 일수 (윤년은 고려하지 않음)
day_list = [0, 31,28,31,30,31,30,31,31,30,31,30,31]

# 요일 리스트 (정상 순서)
weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# 기준일: 1월 1일은 Monday → index = 1
start_day_index = weekdays.index("Mon")

# 기준일부터 목표일까지 며칠 차이 나는지 계산
total_days = 0

# 출력
if m1 == m2:
    total_days = d2 - d1
else:
    # 시작 달의 남은 날짜
    total_days += day_list[m1] - d1
    # 중간 달들
    for m in range(m1 + 1, m2):
        total_days += day_list[m]
    # 마지막 달의 날짜
    total_days += d2

target_day_index = (start_day_index + total_days) % 7
print(weekdays[target_day_index])
