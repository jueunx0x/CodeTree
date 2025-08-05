n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

jump_x,jump_y = [],[]
length = 0 
md_arr = []
sum = 0
# Please write your code here.
for i in range(1,len(x)-1):
    jump_x = x[:i] + x[i+1:]
    jump_y = y[:i] + y[i+1:]
    for j in range(1,len(jump_x)):
        sum += abs(jump_x[j-1]-jump_x[j]) + abs(jump_y[j-1]-jump_y[j])
    md_arr.append(sum)
    sum = 0
print(min(md_arr))