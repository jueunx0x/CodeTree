n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class Student:
    def __init__(self,h,w,seq):
        self.seq = seq
        self.h = h
        self.w = w
    def __str__(self):
        return f"{self.h} {self.w} {self.seq}"

students_sort = []
for i in students:
    a,b,c = i
    students_sort.append(Student(a,b,c))

students_sort.sort(key = lambda x:(x.h,- x.w))

for i in students_sort:
    print(i)