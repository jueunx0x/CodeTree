n = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if A[i] <= A[j] <= A[k] :
                count += 1

print(count)