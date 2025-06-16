N = int(input())

# Please write your code here.

def f(N):
    if N < 10:
        return N**2
    return f(N//10) + f(N%10)

print(f(N))