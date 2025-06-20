unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class BombClear:
    def __init__(self,code,color,sec):
        self.code = code
        self.color = color 
        self.sec = sec

firstBomb = BombClear(unlock_code,wire_color,seconds)

print("code :",firstBomb.code)
print("color :",firstBomb.color)
print("second :",firstBomb.sec)