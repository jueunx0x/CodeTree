n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

current,result = [],[]
for i in range(n):
    current.append(arr[i])
    current.sort()
    if (i+1)%2 == 1 : 
        mid = len(current)//2
        result.append(str(current[mid]))

result_str = ' '.join(result)
print(result_str)