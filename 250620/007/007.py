secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class A:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time

A1 = A(secret_code,meeting_point,time)
print("secret code :",A1.code)
print("meeting point :",A1.place)
print("time :",A1.time)