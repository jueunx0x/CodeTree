n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
start,end = 0,0
events = []
for i in segments:
    start,end = i
    events.append((start,1))
    events.append((end,-1))

events.sort(key=lambda x: (x[0], -x[1]))


current = 0
max_overlap = 0


for x,delta in events:
    current += delta
    max_overlap = max(current,max_overlap)

print(max_overlap)