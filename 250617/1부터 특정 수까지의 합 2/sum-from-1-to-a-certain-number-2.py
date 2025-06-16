N = int(input())

# Please write your code here.

def f(N):
    if N == 1:
        return 1
    return f(N-1) + N

print(f(N))