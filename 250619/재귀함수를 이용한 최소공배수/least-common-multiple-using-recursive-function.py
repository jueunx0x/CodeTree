n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(n):
    global arr
    if n == 0 :
        return 1
    else:
        return f(n-1) * arr[n-1]
        
    if arr[n] % 2 == 0:
        return arr[n]//2
    elif arr[n] % 3 == 0:
        return arr[n]//3
    else : return arr[n]

    
print(f(n-1))