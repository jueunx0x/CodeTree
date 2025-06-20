n = int(input())
class RainyDay:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather
    def __str__(self):
        return f"{self.date} {self.day} {self.weather}" #문자열 출력 부분 

days = []
for _ in range(n):
    d, dy, w = input().split()
    #date.append(d)
    #day.append(dy)
    #weather.append(w)
    days.append(RainyDay(d,dy,w))

# Please write your code here.
rain_days = [day for day in days if day.weather == "Rain"]
min_rain_day = min(rain_days,key = lambda day:day.date) 

print(min_rain_day)