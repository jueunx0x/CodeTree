n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

a,b = 0,0
block = [0]* n
# Please write your code here.
for i in commands:
    a,b = i 
    for j in range(a,b+1):
        block[j]+=1

print(max(block))

