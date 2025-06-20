m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

def day_of_num(m,d):    
    total_day = 0
    days_list = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,m):
        total_day += days_list[m]
    total_day += d 
    return total_day

diff = 0
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
diff = day_of_num(m2,d2) - day_of_num(m1,d2)
check = 0
check = diff//7
diff = diff%7
if diff >= weekdays.index(A):
    check+=1
print(check)