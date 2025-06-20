user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self,userId = "codetree",lv = 10):
        self.userId = userId
        self.lv = lv

user1 = User()
user2 = User("hello",28)
print("user",user1.userId,"lv",user1.lv)
print("user",user2.userId,"lv",user2.lv)