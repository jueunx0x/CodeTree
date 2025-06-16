N = int(input())

# Please write your code here.
def f(N):
    if N == 0 :
        return
    
    print(N,end =" ")
    f(N-1)
    print(N, end = " ")
f(N)