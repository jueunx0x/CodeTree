a, b, c, d = map(int, input().split())

# Please write your code here.
hour,minute = a,b
total_minute = 0
while True :
    if hour == c and minute == d:
        break
    
    if minute == 60 :
        hour += 1
        minute = 0
    
    total_minute += 1
    minute += 1

print(total_minute)
