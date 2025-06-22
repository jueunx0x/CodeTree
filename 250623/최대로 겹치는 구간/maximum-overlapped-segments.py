n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
events = []
for i in segments:
    a,b = i
    events.append((a, 1))      # 구간 시작
    events.append((b, -1)) # 구간 종료 (r을 포함하지 않게 하려면 +1)

events.sort()

current = 0
max_overlap = 0

for x, delta in events:
    current += delta
    max_overlap = max(max_overlap, current)

print(max_overlap)