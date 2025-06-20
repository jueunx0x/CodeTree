n = int(input())
class student:
    def __init__(self,n,h,w):
        self.n = n
        self.h = h
        self.w = w
    def __str__(self):
        return f"{self.n} {self.h} {self.w}"

students = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    students.append(student(n_i,h_i,w_i))


students.sort(key = lambda x : x.h)
for i in students:
    print(i)
# Please write your code here.