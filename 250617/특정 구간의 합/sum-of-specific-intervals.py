n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def suyeol(n,m):
    global arr,queries
    
    for i in queries:
        a,b = i
        sum = 0
        for j in range(a-1,b):
            sum+=arr[j]
        print(sum)

suyeol(n,m)