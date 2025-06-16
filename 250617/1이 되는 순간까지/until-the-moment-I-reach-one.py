N = int(input())
count = 0
# Please write your code here.
def f(N):
    global count
    if N == 1 :
        return count
    elif N % 2 == 0 :
        count += 1
        return f(N//2)

    else:
        count += 1
        return f(N//3) 

print(f(N))