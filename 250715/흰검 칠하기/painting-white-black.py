OFFSET = 1000
SIZE = 4000  # 충분한 배열 크기 확보

n = int(input())
cur = 0

# 각 칸마다 white/black 횟수 기록
white = [0] * SIZE
black = [0] * SIZE
last = [''] * SIZE  # 마지막 칠한 색

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(cur - x, cur):
            idx = i + OFFSET
            white[idx] += 1
            last[idx] = 'W'
        cur -= x
    else:  # R
        for i in range(cur, cur + x):
            idx = i + OFFSET
            black[idx] += 1
            last[idx] = 'B'
        cur += x

# 결과 집계
w_cnt, b_cnt, g_cnt = 0, 0, 0

for i in range(SIZE):
    if white[i] >= 2 and black[i] >= 2:
        g_cnt += 1
    elif white[i] or black[i]:
        if last[i] == 'W':
            w_cnt += 1
        else:
            b_cnt += 1

print(w_cnt, b_cnt, g_cnt)
