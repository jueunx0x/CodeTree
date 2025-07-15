n = int(input())
A = list(map(int, input().split()))

arr = []
total_len = []
# Please write your code here.

for i in range(1,n+1) :
    arr.append(i)

for i in range(len(arr)):
    sum = 0
    for j in range(len(A)):
        sum += abs((arr[i]-arr[j]))*A[j]
    total_len.append(sum)
print(min(total_len))