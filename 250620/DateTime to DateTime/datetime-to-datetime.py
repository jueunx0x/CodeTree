a, b, c = map(int, input().split())

# Please write your code here.

def time_check(a,b,c):
    day,hour,minute = 11,11,11
    total_min = 0

    if a<= 11 and b < 11  :
        return -1
    while True:
        if day == a and hour == b and minute == c:
            break
        if hour == 24 :
            day+=1
            hour = 0
        if minute == 60 :
            hour += 1
            minute = 0
        minute +=1
        total_min += 1
    return total_min

print(time_check(a,b,c))